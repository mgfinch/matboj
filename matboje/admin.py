from django.contrib import admin
from matboje.models import Matboj, MatbojCompetitors


class CompetitorsInline(admin.TabularInline):
    model = MatbojCompetitors
    extra = 6
    
class MatbojAdmin(admin.ModelAdmin):
    
    fields = ['name','date']
    inlines = [CompetitorsInline]
    list_display = ['name','competitors_count','date']
    
    def competitors_count(self, inst):
    	return len(MatbojCompetitors.objects.filter(matboj=inst))

admin.site.register(Matboj,MatbojAdmin)

