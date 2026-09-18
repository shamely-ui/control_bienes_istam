# Importamos las herramientas para crear tablas en la base de datos
from django.db import models
# Permite mostrar mensajes de error cuando un dato no es válido
from django.core.exceptions import ValidationError

# ==========================
# VALIDACIÓN DE CÉDULA ECUATORIANA
# ==========================
# Comprueba que la cédula ingresada tenga una estructura válida
def validar_cedula_ecuatoriana(cedula):

    # La cédula debe contener exactamente 10 números
    if not cedula.isdigit() or len(cedula) != 10:
        raise ValidationError(
            'La cédula debe contener exactamente 10 números.'
        )

    # Los dos primeros números corresponden al código de provincia
    provincia = int(cedula[:2])

    # Ecuador utiliza códigos provinciales del 01 al 24
    # y el código 30 para ecuatorianos registrados en el exterior
    if provincia < 1 or (provincia > 24 and provincia != 30):
        raise ValidationError(
            'El código de provincia de la cédula no es válido.'
        )

    # El tercer dígito debe ser menor que 6 para una persona natural
    if int(cedula[2]) >= 6:
        raise ValidationError(
            'La cédula ingresada no corresponde a una persona natural.'
        )

    # Convertimos cada carácter de la cédula en un número
    digitos = [int(numero) for numero in cedula]

    # Coeficientes utilizados para validar una cédula ecuatoriana
    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]

    suma = 0

    # Multiplicamos los primeros 9 dígitos por sus coeficientes
    for i in range(9):
        resultado = digitos[i] * coeficientes[i]

        # Si el resultado es mayor o igual a 10, se resta 9
        if resultado >= 10:
            resultado -= 9

        suma += resultado

    # Calculamos el dígito verificador esperado
    digito_verificador = (10 - (suma % 10)) % 10

    # Comparamos el resultado con el último número de la cédula
    if digito_verificador != digitos[9]:
        raise ValidationError(
            'La cédula ecuatoriana ingresada no es válida.'
        )

# ==========================
# TABLA: CATEGORÍAS
# ==========================
# Aquí se almacenarán los tipos de bienes del instituto
# Ejemplo: Computadoras, Mobiliario, Impresoras, etc.
class Categoria(models.Model):

    # Nombre de la categoría (máximo 100 caracteres)
    nombre = models.CharField(max_length=100)

    # Descripción opcional de la categoría
    descripcion = models.TextField(blank=True, null=True)

    # Estado para activar o desactivar categorías
    activo = models.BooleanField(default=True)

    # Fecha en la que fue creada
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Muestra el nombre cuando la categoría aparezca en Django
    def __str__(self):
        return self.nombre

# ==========================
# TABLA: UBICACIONES
# ==========================
# Guarda los lugares físicos donde pueden encontrarse los bienes del instituto
class Ubicacion(models.Model):

    # Nombre de la ubicación
    # Ejemplo: Rectorado, Biblioteca, Laboratorio de Software
    nombre = models.CharField(max_length=150)

    # Descripción adicional de la ubicación
    # Este campo es opcional
    descripcion = models.TextField(blank=True, null=True)

    # Permite activar o desactivar una ubicación sin eliminarla
    activo = models.BooleanField(default=True)

    # Guarda automáticamente la fecha en que se registró la ubicación
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Permite que Django muestre el nombre de la ubicación
    def __str__(self):
        return self.nombre

# ==========================
# TABLA: CUSTODIOS
# ==========================
# Guarda la información de las personas responsables de los bienes
class Custodio(models.Model):

    # Número de cédula del custodio
    # unique=True evita que se registre la misma cédula dos veces
    cedula = models.CharField(max_length=10,
     unique=True,
     validators=[validar_cedula_ecuatoriana]
     )

    # Nombres del custodio
    nombres = models.CharField(max_length=100)

    # Apellidos del custodio
    apellidos = models.CharField(max_length=100)

    # Cargo que ocupa dentro del instituto
    # Ejemplo: Docente, Secretaria, Coordinador
    cargo = models.CharField(max_length=100)

    # Departamento o área a la que pertenece
    # Ejemplo: Rectorado, Secretaría, Sistemas
    departamento = models.CharField(max_length=100)

    # Correo electrónico
    # Puede dejarse vacío si no se dispone del dato
    correo = models.EmailField(blank=True, null=True)

    # Número de teléfono
    # Puede dejarse vacío
    telefono = models.CharField(max_length=15, blank=True, null=True)

    # Ciclo del estudiante
    ciclo = models.CharField(
        max_length=50,
        blank=True,
        null=True
)

    # Carrera del estudiante
    carrera = models.CharField(
        max_length=150,
        blank=True,
        null=True
)

    # Dirección del estudiante
    direccion = models.CharField(
     max_length=200,
     blank=True,
     null=True
)



    # Permite activar o desactivar al custodio sin eliminarlo
    activo = models.BooleanField(default=True)

    # Fecha en la que se registró el custodio
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Muestra nombres y apellidos cuando Django utilice este registro
    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


# ==========================
# TABLA: BIENES
# ==========================
# Guarda la información de cada bien que pertenece al instituto
class Bien(models.Model):
# Código institucional, puede quedar pendiente
    codigo = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True
    )

    # Nombre o descripción principal
    nombre = models.CharField(max_length=150)

    # Categoría
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='bienes'
    )

    # Ubicación
    ubicacion = models.ForeignKey(
        Ubicacion,
        on_delete=models.PROTECT,
        related_name='bienes'
    )

    # Tipo de bien: BLD o BCA
    tipo_bien = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    # Marca
    marca = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    # Modelo
    modelo = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    # Serie
    serie = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    # Valor de compra
    valor_compra = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    # Color
    color = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    # Material
    material = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    # Características generales
    caracteristicas = models.TextField(
        blank=True,
        null=True
    )

    # Dimensiones
    alto = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True
    )

    ancho = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True
    )

    profundidad = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True
    )

    # Estado físico
    ESTADOS = [
        ('BUENO', 'Bueno'),
        ('REGULAR', 'Regular'),
        ('MALO', 'Malo'),
    ]

    estado = models.CharField(
        max_length=10,
        choices=ESTADOS,
        default='BUENO'
    )

    # Observaciones
    observaciones = models.TextField(
        blank=True,
        null=True
    )

    # Datos originales proporcionados por el ISTAM
    valor_compra_original = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    dimensiones_originales = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    condicion_original = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    ubicacion_original = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    custodio_original = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    # Datos adicionales del documento original
    datos_adicionales_originales = models.TextField(
        blank=True,
        null=True
    )

    # Procedencia del bien
    PROCEDENCIAS = [
        ('COMPRADO', 'Comprado'),
        ('DONADO', 'Donado'),
]

    procedencia = models.CharField(
        max_length=20,
        choices=PROCEDENCIAS,
        blank=True,
        null=True
)


    # Indica si sigue activo
    activo = models.BooleanField(default=True)

    # Fecha de creación
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

# ==========================
# TABLA: ASIGNACIONES
# ==========================
# Registra la entrega de un bien a un custodio
class Asignacion(models.Model):

    # Bien que se entrega
    bien = models.ForeignKey(
        Bien,
        on_delete=models.PROTECT,
        related_name='asignaciones'
    )

    # Persona responsable del bien
    custodio = models.ForeignKey(
        Custodio,
        on_delete=models.PROTECT,
        related_name='asignaciones'
    )

    # Número de acta
    numero_acta = models.CharField(
        'Número de acta',
        max_length=30,
        blank=True,
        null=True
    )

   # Fecha de entrega
# Puede quedar pendiente si el documento no contiene la fecha
    fecha_asignacion = models.DateField(
        blank=True,
        null=True
)

    # Fecha de devolución, si existe
    fecha_devolucion = models.DateField(
        blank=True,
        null=True
    )

    # Observaciones opcionales
    observaciones = models.TextField(
        blank=True,
        null=True
    )

    # Indica si la asignación sigue vigente
    activa = models.BooleanField(default=True)

    # Fecha de registro
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Texto que mostrará Django
    def __str__(self):
        return f"{self.bien.codigo} - {self.custodio}"
# ==========================
# TABLA: CONSTATACIONES
# ==========================
class Constatacion(models.Model):

    # Bien revisado
    bien = models.ForeignKey(
        Bien,
        on_delete=models.PROTECT,
        related_name='constataciones'
    )

    # Fecha de la revisión
    fecha_constatacion = models.DateField()

    # Estado encontrado
    estado_encontrado = models.CharField(
        max_length=10,
        choices=Bien.ESTADOS
    )

    # Indica si el bien fue encontrado
    encontrado = models.BooleanField(default=True)

    # Observaciones
    observaciones = models.TextField(
        blank=True,
        null=True
    )

    # Fecha de registro
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bien.codigo} - {self.fecha_constatacion}"  


# ==========================
# TABLA: BAJAS
# ==========================
class Baja(models.Model):

    # Bien dado de baja
    bien = models.ForeignKey(
        Bien,
        on_delete=models.PROTECT,
        related_name='bajas'
    )

    # Motivo de la baja
    motivo = models.CharField(max_length=200)

    # Fecha de la baja
    fecha_baja = models.DateField()

    # Observaciones
    observaciones = models.TextField(
        blank=True,
        null=True
    )

    # Fecha de registro
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bien.codigo} - {self.fecha_baja}"