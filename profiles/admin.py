from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """
    Created to handle the profiles 
    """
    list_display = ("pk", "user", "bio", "image")


admin.site.register(Profile, ProfileAdmin)
