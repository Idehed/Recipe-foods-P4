from django.contrib import admin
from .models import Recipe, CommentRecipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """
    Created to handle the recipe posts
    """
    list_display = (
        "title",
        "meal_type",
        "calories",
        "instructions",
        "ingredients",
        "image",
    )
    list_filter = ("meal_type",)


admin.site.register(CommentRecipe)
