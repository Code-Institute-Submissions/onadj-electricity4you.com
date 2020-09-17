from django.contrib import admin
from .models import Deliverycost, Country

# Register your models here.

class DeliverycostAdmin(admin.ModelAdmin):
    list_display = (
        'country',
        'sku',
        'name',
        'description',
        'price',
    )

ordering = ('sku', )

class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Deliverycost, DeliverycostAdmin)
admin.site.register(Country, CountryAdmin)
