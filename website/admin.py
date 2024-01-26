from django.contrib import admin
from .models import Information, Developer, About, Contact
# Register your models here.

class WebsiteAdminModel(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'phone_number')
    list_filter = ('name', 'email', 'address', 'phone_number',)
    search_fields = ('name', 'email','address', 'phone_number',)

class DeveloperAdminModel(admin.ModelAdmin):
    list_display = ('name','email')
    list_filter = ('name','email',)
    search_fields = ('name','email',)

class AboutAdminModel(admin.ModelAdmin):
    list_display = ('name', 'description', 'photo')
    list_filter = ('name',)
    search_fields = ('name',)

class ContactAdminModel(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    list_filter = ('name', 'email', 'subject',)
    search_fields = ('name',)
    
admin.site.register(Information, WebsiteAdminModel)
admin.site.register(Developer, DeveloperAdminModel)
admin.site.register(About, AboutAdminModel)
admin.site.register(Contact, ContactAdminModel)
