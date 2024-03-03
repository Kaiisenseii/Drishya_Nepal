from django.contrib import admin
from . models import Hire, Testimonial
# Register your models here.

class HireAdmin(admin.ModelAdmin):
    list_display = ('customer', 'photographer','status','location', 'date', 'service' , 'description')
    list_filter = ('location', 'date',)
    search_fields = ('location', 'date', 'service',)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'logo')
    list_filter = ('name', 'description',)
    search_fields = ('name',)

admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Hire, HireAdmin)