from django.db import models

# Create your models here.
class DatabaseInformation(models.Model):

    id1 = models.TextField()
    name = models.TextField()
    description = models.TextField()