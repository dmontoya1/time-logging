from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """
    Clase para almacenar las categorías de cada registro
    """

    name = models.CharField(
        "Nmobre",
        max_length=255
    )
    parent = models.ForeignKey(
        "self",
        verbose_name="Categoría Padre",
        on_delete=models.SET_NULL,
        related_name="categories",
        null=True,
        blank=True
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Categoría"
        ordering = ['name', ]

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
