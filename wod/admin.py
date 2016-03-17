from django.contrib import admin

from .models import Wod, WeightLifting


class WodInline(admin.TabularInline):
    model = Wod

class WodAdmin(admin.ModelAdmin):
#    fields = ['warm_up','weightlifting','metcon','strength_accessory']



    date_hierarchy = 'date'
    fieldsets = [
        ('Warm Up',               {'fields': ['warm_up']}),
        ('Weightlifting',                {'fields': ['weightlifting']}),
        ('Metcon', {'fields': ['metcon']}),
        ('Strength Accessory', {'fields':['strength_accessory']}),
    ]

    list_display = ('date',)

class WeightLiftingAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Movement',               {'fields': ['movement']}),
        ('rep_scheme',                {'fields': ['rep_scheme']}),
        ('description', {'fields': ['description']}),
        ('date', {'fields':['date']}),
    ]

    list_display = ('date',)

admin.site.register(Wod, WodAdmin)
admin.site.register(WeightLifting, WeightLiftingAdmin)
