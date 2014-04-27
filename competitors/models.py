from django.db import models

# Create your models here.
class Druzina(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    
    def __unicode__(self):
        return self.name
    
class Competitor(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    druzina = models.ForeignKey(Druzina)

    def __unicode__(self):
        return self.name
