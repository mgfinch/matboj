from django.contrib import admin
from competitors.models import Competitor, Druzina
from matboje.models import Matboj

class CompetitorsInline(admin.StackedInline):
    model = Competitor
    extra = 3


class DruzinaAdmin(admin.ModelAdmin):

    fields = ['name']
    inlines = [CompetitorsInline]

admin.site.register(Druzina, DruzinaAdmin)

class MatbojsInline(admin.StackedInline):
    model = Matboj.competitors.through
    extra = 0
    
class CompetitorAdmin(admin.ModelAdmin):

    fields = ['name','druzina']
    inlines = [MatbojsInline]

admin.site.register(Competitor, CompetitorAdmin)
