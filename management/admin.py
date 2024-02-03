from django.contrib import admin
from . models import Hire
# Register your models here.

class HireAdmin(admin.ModelAdmin):
    list_display = ('customer', 'photographer','location', 'date', 'service' , 'description')
    list_filter = ('location', 'date',)
    search_fields = ('location', 'date', 'service',)

class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name','description', 'logo')
    list_filter = ('name', 'description')
    search_fields = ('name',)

admin.site.register(Hire, HireAdmin)