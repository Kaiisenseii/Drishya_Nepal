from django.contrib import admin
from . models import Photo, Equipment, Photographer, Services, Tag
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'location','description', 'photo')
    list_filter = ('name', 'location',)
    search_fields = ('name', 'location',)

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
    list_display = ('user', 'experience' , 'is_available')
    list_filter = ( 'experience' , 'is_available')
    search_fields = ( 'experience' , 'is_available')
    
    inlines = [PhotoInline, EquipmentInline, ServicesInline]
    @admin.display(ordering='photographer__user', description='User')
    def get_user(self, obj):
        return obj.user.get_full_name()


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Photographer, PhotographerAdmin)
admin.site.register(Tag)    