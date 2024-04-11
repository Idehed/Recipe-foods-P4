from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display= (
        'title',
        'meal_types',
        'calories',
        'instructions',
        'ingredients',
        'image'
    )
    list_filter = ('meal_type',)
