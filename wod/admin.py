from django.contrib import admin

from .models import Wod, WeightLifting, Athlete


class WodInline(admin.TabularInline):
    """Formats the administrative display for Wod objects.

    Inherits from django's admin.TabularInline and uses Wod objects for its
    model.
    """

    model = Wod

class WodAdmin(admin.ModelAdmin):
    """Determines which fields to display for Wod objects in the admin.

    Inherits from django's admin.ModelAdmin filters and displays objects based
    off of a Wod's date field.  The fieldsets attribute is a list that contains
    all of the attributes that are to be displayed.  list_display is used to
    display each individual workout in the admin, in this case the date is
    used.
    """

    date_hierarchy = 'date'
    fieldsets = [
        ('Warm Up',               {'fields': ['warm_up']}),
        ('Weightlifting',                {'fields': ['weightlifting']}),
        ('Metcon', {'fields': ['metcon']}),
        ('Strength Accessory', {'fields':['strength_accessory']}),
    ]

    list_display = ('date',)


class WeightLiftingAdmin(admin.ModelAdmin):
    """Determines which fields to display for WeightLifting objects in the admin.

    Inherits from django's admin.ModelAdmin filters and displays weightlifting
    objects.  The fieldsets attribute is a list that contains all of the
    attributes that are to be displayed.  list_display is used to display each
    individual workout in the admin, in this case the date is used.
    """

    fieldsets = [

        ('Movement',               {'fields': ['movement']}),
        ('rep_scheme',                {'fields': ['rep_scheme']}),
        ('description', {'fields': ['description']}),
        ('date', {'fields':['date']}),
    ]

    list_display = ('date',)


class AthleteAdmin(admin.ModelAdmin):
    """Determines which fields to display for Athlete objects in the admin.

    Inherits from django's admin.ModelAdmin filters and displays athlete
    objects.  The fieldsets attribute is a list that contains all of the
    attributes that are to be displayed.  list_display is used to display each
    individual workout in the admin, in this case the athlete is used.
    """
    fieldsets = [
        ('Workouts Completed',               {'fields': ['workouts_completed']}),
        ('Personal Records',                {'fields': ['personal_records']}),
        ('Favorite Movement', {'fields': ['favorite_movement']}),
        ('Athlete', {'fields':['athlete']}),
    ]

    list_display = ('athlete',)


"""
Register all of the models with django, this tells django hey use this model
with this customized admin class.
"""

# Register the Wod model to the WodAdmin.
admin.site.register(Wod, WodAdmin)

# Register the WeightLifting model to the WeightLiftingAdmin.
admin.site.register(WeightLifting, WeightLiftingAdmin)

# Register the Athlete model to the AthleteAdmin.
admin.site.register(Athlete, AthleteAdmin)
