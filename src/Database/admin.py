from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import DatabaseInformation
from import_export import resources

#admin.site.register(DatabaseInformation)
# Register your models here.
@admin.register(DatabaseInformation)
class BeerAdmin(ImportExportModelAdmin):
    pass