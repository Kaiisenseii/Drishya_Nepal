from django.contrib import admin
from . models import Photo, Equipment, Photographer, Services, Tag
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'location','description', 'type', 'date_taken', 'photo')
    list_filter = ('name', 'location', 'date_taken', 'type','date_taken',)
    search_fields = ('name', 'location', 'type',)

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'photo')
    list_filter = ('name', 'description',)
    search_fields = ('name',)    

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'duration')
    list_filter = ('name', 'description' ,'price', 'duration')
    search_fields = ('name', 'duration')


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1

class EquipmentInline(admin.StackedInline):
    model = Equipment
    extra = 1

class ServicesInline(admin.StackedInline):
    model = Services
    extra = 1


class PhotographerAdmin(admin.ModelAdmin):
    list_display = ( 'experience' , 'is_available')
    list_filter = ( 'experience' , 'is_available')
    search_fields = ( 'experience' , 'is_available')
    
    inlines = [PhotoInline, EquipmentInline, ServicesInline]

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Photographer, PhotographerAdmin)

admin.site.register(Tag)