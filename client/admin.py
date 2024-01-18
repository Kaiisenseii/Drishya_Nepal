from django.contrib import admin
from .models import Customer, Feedback
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','age','address', 'phone_number')
    list_filter = ('address',)
    search_fields = ('name', 'email',)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('message', 'rating')
    list_filter = ('rating',)
    search_fields = ('message',)
    

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Feedback, FeedbackAdmin)