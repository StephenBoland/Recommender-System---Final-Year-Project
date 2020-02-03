from django.db import models

#Beer information database
class DatabaseInformation(models.Model):


    name = models.CharField(max_length=100, null = True)
    description = models.TextField(max_length=500,null = True)
    abv = models.FloatField()
    #img = models.CharField(max_length=100)
    
def __str__(self):
    return self.name

#brewery information database

class BreweryInformation(models.Model):
    name = models.CharField(max_length=100, null = True)
    description = models.TextField(max_length=500, null = True)
    
def __str__(self):
    return self.name
#
##Users information database
#class UserInformation(models.Model):
#    Firstname = models.CharField(max_length=20, null = True)
#    Secondname = models.CharField(max_length=20, null = True)
#    Email = models.EmailField(max_length=50, null = True)
#    Username = models.CharField(max_length=50, null = True)
#    Password= models.CharField(max_length=50,null = True)
#    Confirmpassword = models.CharField(max_length=50, null = True)
#    
    