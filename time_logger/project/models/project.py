from django.db import models

from time_logger.users.models import User


class Project(models.Model):
    """
    Clase para almacenar los proyectos en los que se estará trabajando
    """

    name = models.CharField(
        "Nombre",
        max_length=255
    )
    code = models.CharField(
        "Código o abbr",
        max_length=255,
        null=True,
        blank=True
    )
    leader = models.ForeignKey(
        User,
        verbose_name="Persona a cargo del Proyecto",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Proyecto"
