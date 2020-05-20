from django.contrib import admin

from .models import Action, Device


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    """
    """

    list_display = ('name', )
    search_fields = ('name', )


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    """
    """

    list_display = ('name', 'so_version', )
    search_fields = ('name', )
