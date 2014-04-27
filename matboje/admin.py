from django.contrib import admin
from matboje.models import Matboj


class CompetitorsInline(admin.TabularInline):
    model = Matboj.competitors.through
    extra = 6
    
class MatbojAdmin(admin.ModelAdmin):

    fields = ['name']
    inlines = [CompetitorsInline]

admin.site.register(Matboj,MatbojAdmin)
