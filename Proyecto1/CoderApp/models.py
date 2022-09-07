from django.db import models
from datetime import date, datetime
from datetime import date
 
class mascotas(models.Model):
    nombre= models.CharField(max_length=50)
    parentesco= models.CharField(max_length=50)
    edad= models.IntegerField()
    cumpleanios= models.DateField(blank=True, null=True)

# Create your models here.
#, default=date.today()