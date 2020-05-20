from django.db import models

from .project import Project


class SubProject(models.Model):
    """
    Clase para guardar los subprojectos
    """

    name = models.CharField(
        "Nombre",
        max_length=255
    )
    project = models.ForeignKey(
        Project,
        verbose_name="Proyecto",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "SubProyecto"
