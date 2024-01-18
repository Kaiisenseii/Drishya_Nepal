from django.contrib import admin
from . models import Hire
# Register your models here.

class HireAdmin(admin.ModelAdmin):
    list_display = ('location', 'date', 'price' , 'description')
    list_filter = ('location', 'date',)
    search_fields = ('location', 'date', 'price',)

admin.site.register(Hire, HireAdmin)