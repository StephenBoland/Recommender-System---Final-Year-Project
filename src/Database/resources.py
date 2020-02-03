from import_export import resources
from .models import DatabaseInformation

class BeerInformation (resources.ModelResource):
    class Meta:
        mode1 = Beer
        


class BreweryInformation (resources.ModelResource):
    class Meta:
        mode1 = Brewery