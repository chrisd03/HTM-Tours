from django.contrib import admin
from .models import *

class Liked_ActivityInLine(admin.TabularInline):
    model = Liked_Activities
    extra = 1

@admin.register(Tourist)
class TouristAdmin(admin.ModelAdmin):
    inlines = [Liked_ActivityInLine]

@admin.register(Tour_Guide)
class TourGuideAdmin(admin.ModelAdmin):
    inlines = [Liked_ActivityInLine]

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Acceptances)