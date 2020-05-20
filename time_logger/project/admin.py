from django.contrib import admin

from .models import ProjectType, Project, SubProject


class SubProjectStackedAdmin(admin.StackedInline):
    """
    """

    model = SubProject
    extra = 0


class ProjectTypeStackedAdmin(admin.StackedInline):
    """
    """

    model = ProjectType
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    """

    list_display = ('name', 'code', 'leader')
    inlines = [SubProjectStackedAdmin, ProjectTypeStackedAdmin, ]
    search_fields = ('name', 'code', )
