from django.db import models


class Action(models.Model):
    """
    Clase para guardar las acciones que se realizan por cada proyecto
    Ejm: Re Test, diseño plan de pruebas, Ejecución pruebas, etc
    """

    name = models.CharField(
        "Nombre",
        max_length=255
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Acción"
        verbose_name_plural = "acciones"
