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

class Categoria(models.Model):

    # Nombre de la categoría
    nombre = models.CharField(max_length=100)

    # Descripción opcional
    descripcion = models.TextField(
        blank=True,
        null=True
    )

    # Permite activar o desactivar
    activo = models.BooleanField(default=True)

    # Fecha de creación
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


# ==========================
# TABLA: UBICACIONES
# ==========================

class Ubicacion(models.Model):

    # Nombre de la ubicación
    nombre = models.CharField(max_length=150)

    # Descripción opcional
    descripcion = models.TextField(
        blank=True,
        null=True
    )

    # Permite activar o desactivar
    activo = models.BooleanField(default=True)

    # Fecha de creación
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


# ==========================
# TABLA: CUSTODIOS
# ==========================

class Custodio(models.Model):

    # Número de cédula
    cedula = models.CharField(
        max_length=10,
        unique=True,
        validators=[validar_cedula_ecuatoriana]
    )

    # Nombres
    nombres = models.CharField(max_length=100)

    # Apellidos
    apellidos = models.CharField(max_length=100)

    # Cargo
    cargo = models.CharField(max_length=100)

    # Departamento o área
    departamento = models.CharField(max_length=100)

    # Correo electrónico
    correo = models.EmailField(
        blank=True,
        null=True
    )

    # Teléfono
    telefono = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

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

    # Dirección
    direccion = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    # Permite activar o desactivar
    activo = models.BooleanField(default=True)

    # Fecha de creación
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


# ==========================
# TABLA: BIENES
# ==========================

class Bien(models.Model):

    # Código institucional
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

    # Fotografía opcional del bien
    foto = models.ImageField(
        upload_to='bienes/',
        blank=True,
        null=True
    )

# Fecha de creación
fecha_creacion = models.DateTimeField(auto_now_add=True)


# ==========================
# TABLA: ASIGNACIONES
# ==========================

# Permite entregar uno o varios bienes a un custodio
class Asignacion(models.Model):

    # Campo antiguo
    # Se conserva temporalmente para mantener los registros anteriores
    bien = models.ForeignKey(
        Bien,
        on_delete=models.PROTECT,
        related_name='asignaciones',
        blank=True,
        null=True
    )

    # Permite incluir varios bienes en una misma asignación
    bienes = models.ManyToManyField(
        Bien,
        related_name='asignaciones_multiples',
        blank=True
    )

    # Persona responsable de los bienes
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
    fecha_asignacion = models.DateField(
        blank=True,
        null=True
    )

   # Fecha prevista para devolver los bienes
    fecha_prevista_devolucion = models.DateField(
        'Fecha prevista de devolución',
        blank=True,
        null=True
)

# Fecha en que los bienes fueron devueltos realmente
    fecha_devolucion = models.DateField(
        'Fecha de devolución real',
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

    def __str__(self):
        return f"Asignación {self.id} - {self.custodio}"


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

    # Fecha de revisión
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

    # Fecha de baja
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