from django.db import models
from competitors import settings

# Create your models here.
class Druzina(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    
    def __str__(self):
        return self.name

class Competitor(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    druzina = models.ForeignKey(Druzina)

    def name_reversed(self):
        return " ".join(self.name.split(" ")[::-1])

    def __str__(self):
        return self.name_reversed() if settings.COMPETITORS_NAME_REVERSED else self.name

    class Meta:
        ordering = ['name']
