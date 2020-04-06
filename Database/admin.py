from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import DatabaseInformation, BreweryInformation,Stouts,Ales,Porters,Largers,NonAlcoholic
from import_export import resources

#admin.site.register(DatabaseInformation)
# Register your models here.
@admin.register(DatabaseInformation)
class BeerAdmin(ImportExportModelAdmin):
    pass

@admin.register(BreweryInformation)
class BreweryAdmin(ImportExportModelAdmin):
    pass
@admin.register(Stouts)
class BreweryAdmin(ImportExportModelAdmin):
    pass
@admin.register(Ales)
class BreweryAdmin(ImportExportModelAdmin):
    pass
@admin.register(Porters)
class BreweryAdmin(ImportExportModelAdmin):
    pass
@admin.register(Largers)
class BreweryAdmin(ImportExportModelAdmin):
    pass
@admin.register(NonAlcoholic)
class BreweryAdmin(ImportExportModelAdmin):
    pass
