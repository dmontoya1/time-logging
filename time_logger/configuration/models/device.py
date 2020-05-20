
from django.db import models


class Device(models.Model):
    """
    Clase para guardar los dispositivos de ejecución
    """

    name = models.CharField(
        "Nombre",
        max_length=255,
        help_text="iPhone 7, Samsung S8, Chrome, Chrome Mac, Mozilla, Safari"
    )
    so_version = models.CharField(
        "Versión Sistema Operativo (si aplica)",
        max_length=255,
        help_text="iOS 12.4.1, Android 9.",
        null=True,
        blank=True
    )

    def __str__(self):
        if self.so_version:
            return "{} {}".format(self.name, self.so_version)
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Dispositivo"
        ordering = ['name', ]
