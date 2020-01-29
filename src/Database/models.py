from django.db import models

# Create your models here.
class DatabaseInformation(models.Model):


    name = models.CharField(max_length=100, null = True)
    description = models.TextField(max_length=500,null = True)
    abv = models.FloatField()
    #img = models.CharField(max_length=100)
    
#class Meta:
 #   ordering = ('name',)
    
def __str__(self):
    return self.name