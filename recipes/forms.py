from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe, CommentRecipe


class RecipeForm(forms.ModelForm):
    """
    Form for the create a recipe page
    """

    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "ingredients",
            "instructions",
            "image",
            "image_description",
            "meal_type",
            "calories",
        ]

        ingredients = forms.CharField(widget=RichTextWidget())
        instructions = forms.CharField(widget=RichTextWidget())

        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "title": "Recipe Title",
            "description": "Description",
            "ingredients": "Recipe Ingredients",
            "instructions": "Recipe Instructions",
            "image": "Recipe Image",
            "image_description": "Describe Image",
            "meal_type": "Meal Type",
            "calories": "Calories",
        }


class CommentRecipeForm(forms.ModelForm):
    """
    Form for creating comments on a recipe page
    """
    class Meta:
        model = CommentRecipe
        fields =('body',)