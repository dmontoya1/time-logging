from django.db import models

from .project import Project
from .sub_project import SubProject


class ProjectType(models.Model):
    """

    """
    name = models.CharField(
        'Nombre',
        max_length=255
    )
    project = models.ForeignKey(
        Project,
        verbose_name="Proyecto",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    sub_project = models.ForeignKey(
        SubProject,
        verbose_name="Subproyecto",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tipo de Proyecto"
        verbose_name_plural = "Tipos de Proyecto"
