from django.contrib import admin

# Register your models here.

from .models import Weather, User

admin.site.register(User)
admin.site.register(Weather)
