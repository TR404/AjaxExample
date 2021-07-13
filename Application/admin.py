from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(Intro)

@admin.register(Intro)
class IntroModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mobile', 'email', 'about']