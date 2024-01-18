from django.contrib import admin
from .models import Website, Developer
# Register your models here.

class WebsiteAdminModel(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'phone_number')
    list_filter = ('name', 'email', 'address', 'phone_number',)
    search_fields = ('name', 'email','address', 'phone_number',)

class DeveloperAdminModel(admin.ModelAdmin):
    list_display = ('name','email')
    list_filter = ('name','email',)
    search_fields = ('name','email',)
    
admin.site.register(Website, WebsiteAdminModel)
admin.site.register(Developer, DeveloperAdminModel)
