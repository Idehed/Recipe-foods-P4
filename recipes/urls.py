from django.urls import path
from .views import (
    AddRecipe, Recipes, 
    RecipeDetail, DeleteRecipe,
    EditRecipe, comment_edit
)
from .import views

urlpatterns = [
    path("add/", AddRecipe.as_view(), name="add_recipe"),
    path("", Recipes.as_view(), name="recipes"),
    path("<slug:pk>/", RecipeDetail, name="recipe_detail"),
    path('<slug:pk>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path("delete/<slug:pk>/", DeleteRecipe.as_view(), name="delete_recipe"),
    path("edit/<slug:pk>/", EditRecipe.as_view(), name= "edit_recipe"),
]
