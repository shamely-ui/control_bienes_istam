from django import forms

# Importamos los modelos
from .models import Categoria, Ubicacion, Custodio, Bien, Asignacion, Constatacion, Baja


# Formulario para registrar categorías
class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria

        # Campos que aparecerán en el formulario
        fields = ['nombre', 'descripcion', 'activo']


# Formulario para registrar y editar ubicaciones
class UbicacionForm(forms.ModelForm):

    class Meta:
        model = Ubicacion
        fields = ['nombre', 'descripcion', 'activo']


# Formulario para registrar custodios
class CustodioForm(forms.ModelForm):

    class Meta:
        model = Custodio

        fields = [
            'cedula',
            'nombres',
            'apellidos',
            'cargo',
            'departamento',
            'correo',
            'telefono',
            'ciclo',
            'carrera',
            'direccion',
            'activo'
        ]

    # Define teléfono y dirección como campos obligatorios
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['telefono'].required = True
        self.fields['direccion'].required = True

# Formulario para importar custodios desde Excel
class ImportarCustodiosForm(forms.Form):

    archivo = forms.FileField(
        label='Seleccione el archivo Excel'
    )

# Formulario para registrar y editar bienes
class BienForm(forms.ModelForm):

    class Meta:
        model = Bien
        fields = '__all__'


# Formulario para registrar asignaciones
class AsignacionForm(forms.ModelForm):

    class Meta:
        model = Asignacion

        # Los bienes se seleccionan con el buscador
        fields = [
            'custodio',
            'numero_acta',
            'fecha_asignacion',
            'fecha_prevista_devolucion',
            'observaciones',
            'activa'
        ]

        # Calendarios para las fechas
        widgets = {
            'fecha_asignacion': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'fecha_prevista_devolucion': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }
# Formulario para registrar constataciones
class ConstatacionForm(forms.ModelForm):

    class Meta:
        model = Constatacion
        fields = '__all__'

        # Calendario para seleccionar la fecha
        widgets = {
            'fecha_constatacion': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }
# Formulario para registrar bajas
class BajaForm(forms.ModelForm):

    class Meta:
        model = Baja
        fields = '__all__'

        # Calendario para seleccionar la fecha
        widgets = {
            'fecha_baja': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }

    # Muestra solamente bienes activos
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['bien'].queryset = Bien.objects.filter(
            activo=True
        )

    # Evita registrar dos bajas del mismo bien
    def clean_bien(self):
        bien = self.cleaned_data.get('bien')

        if bien and Baja.objects.filter(bien=bien).exists():
            raise forms.ValidationError(
                'Este bien ya fue dado de baja.'
            )

        return bien

# Formulario para importar bienes desde Excel
class ImportarBienesForm(forms.Form):
    archivo = forms.FileField(
        label='Seleccione el archivo Excel'
    )

    procedencia = forms.ChoiceField(
        choices=[
            ('COMPRADO', 'Comprado'),
            ('DONADO', 'Donado'),
        ],
        label='Procedencia'
    )