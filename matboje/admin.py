from django.contrib import admin
from matboje.models import Matboj, MatbojCompetitors


class CompetitorsInline(admin.TabularInline):
    model = MatbojCompetitors
    extra = 6
    
class MatbojAdmin(admin.ModelAdmin):
    
    fields = ['name','date']
    inlines = [CompetitorsInline]
    #list_display = ['name','date']

admin.site.register(Matboj,MatbojAdmin)

