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
        fields = '__all__'

        widgets = {
            'fecha_asignacion': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'fecha_devolucion': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }

    # Muestra solo bienes disponibles
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        bienes_ocupados = Asignacion.objects.filter(
            fecha_devolucion__isnull=True
        ).values_list('bien_id', flat=True)

        self.fields['bien'].queryset = Bien.objects.filter(
            activo=True
        ).exclude(
            id__in=bienes_ocupados
        )

    # Evita asignar un bien que aún no ha sido devuelto
    def clean(self):
        cleaned_data = super().clean()

        bien = cleaned_data.get('bien')
        fecha_devolucion = cleaned_data.get('fecha_devolucion')

        if bien and not fecha_devolucion:
            asignacion_activa = Asignacion.objects.filter(
                bien=bien,
                fecha_devolucion__isnull=True
            )

            if self.instance.pk:
                asignacion_activa = asignacion_activa.exclude(
                    pk=self.instance.pk
                )

            if asignacion_activa.exists():
                raise forms.ValidationError(
                    'Este bien ya está asignado a otro custodio.'
                )

        return cleaned_data
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