from django.db import models

from time_logger.category.models import Category
from time_logger.configuration.models import Action, Device
from time_logger.project.models import Project, ProjectType, SubProject
from time_logger.users.models import User


class Logger(models.Model):
    """
    Clase para giardar los registros de los tiempos trabajados
    """

    ILANA = "IL"
    VERITRAN = "VT"
    TELETRABAJO = "TT"

    PLACE_CHOICES = [
        (ILANA, 'Ilana'),
        (VERITRAN, 'VeriTran'),
        (TELETRABAJO, 'TeleTrabajo')
    ]

    date = models.DateField(
        "Fecha",
        auto_now_add=False
    )
    responsible = models.ForeignKey(
        User,
        verbose_name="Responsable",
        on_delete=models.SET_NULL,
        null=True,
        related_name='loggers',
    )
    initial_time = models.TimeField(
        "Hora de inicio",
    )
    end_time = models.TimeField(
        "Hora de finalización"
    )
    project = models.ForeignKey(
        Project,
        verbose_name="Proyecto",
        on_delete=models.SET_NULL,
        null=True,
        related_name="loggers"
    )
    category = models.ForeignKey(
        Category,
        verbose_name="Categoría",
        on_delete=models.SET_NULL,
        null=True,
    )
    place = models.CharField(
        "Lugar de ejecución",
        max_length=2,
        choices=PLACE_CHOICES,
        default=TELETRABAJO
    )
    description = models.TextField(
        "Descripción de la actividad"
    )
    action = models.ForeignKey(
        Action,
        verbose_name="Acción que se realiza",
        on_delete=models.SET_NULL,
        null=True,
        related_name="loggers"
    )
    sub_project = models.ForeignKey(
        SubProject,
        verbose_name="Sub Proyecto",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    project_type = models.ForeignKey(
        ProjectType,
        verbose_name="Tipo de proyecto",
        on_delete=models.SET_NULL,
        null=True,
    )
    activity = models.TextField(
        "Flujo o actividad",
    )
    device = models.ForeignKey(
        Device,
        verbose_name="Dispositivo",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return "Registro {} el {}".format(self.project, self.date)

    def save(self, *args, **kwargs):
        self.description = "{} {} {} {} {} {}".format(
            str(self.action),
            str(self.sub_project),
            str(self.project),
            str(self.project_type),
            str(self.activity),
            str(self.device)
        )
        super(Logger, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Registro"
