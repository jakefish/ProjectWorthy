from django.contrib import admin

from .models import Wod

class WodAdmin(admin.ModelAdmin):
#    fields = ['warm_up','weightlifting','metcon','strength_accessory']
    date_hierarchy = 'date'
    fieldsets = [
        ('Warm Up',               {'fields': ['warm_up'], 'classes':['collapse']}),
        ('Weightlifting',                {'fields': ['weightlifting']}),
        ('Metcon', {'fields': ['metcon']}),
        ('Strength Accessory', {'fields':['strength_accessory']}),
    ]

admin.site.register(Wod, WodAdmin)
