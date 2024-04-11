from django.views.generic import CreateView

from .models import Recipe

class AddRecipe(CreateView):
    """
    Add recipe view
    """
    template_name = 'recipes/add_recipe.html'
    model = Recipe
    sucess_url = '/recipes/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)
