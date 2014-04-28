from django.db import models
from django.forms import ModelForm

# Create your models here.
    
class Matboj(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    date = models.DateTimeField('date played')
    competitors = models.ManyToManyField('competitors.Competitor', through='MatbojCompetitors')
    default_rank = models.IntegerField(default=1000)
    
    def __unicode__(self):
        return self.name

# I wouldn't call this in plural, one instance of this class refers to one Competitor        
class MatbojCompetitors(models.Model):
    competitor = models.ForeignKey('competitors.Competitor')
    matboj = models.ForeignKey(Matboj)
    ranking = models.IntegerField(default=0)

    class Meta:
        # Order decreasingly by the ranking
        ordering = ['-ranking']    
