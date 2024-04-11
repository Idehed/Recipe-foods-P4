from django.urls import path
from .views import Recipe

urlpatterns = [
    path('', AddRecipe.as_view(), name='add_recipe'),
]