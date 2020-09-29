from django.contrib import admin
from .models import Deliverytime, Country

# Register your models here.

class DeliverytimeAdmin(admin.ModelAdmin):
    list_display = (
        'country',
        'name',
        'description',
     
    )


class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Deliverytime, DeliverytimeAdmin)
admin.site.register(Country, CountryAdmin)