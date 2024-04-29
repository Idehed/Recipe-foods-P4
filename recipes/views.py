from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from .models import Recipe, CommentRecipe
from .forms import RecipeForm, CommentRecipeForm


class Recipes(ListView):
    """
    View all recipes
    """

    template_name = "recipes/recipes.html"
    model = Recipe
    context_object_name = "recipes"
    """
    function for the search bar
    """

    def get_queryset(self, **kwargs):
        query = self.request.GET.get("q")
        if query:
            recipes = self.model.objects.filter(
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(ingredients__icontains=query)
                | Q(instructions__icontains=query)
                | Q(meal_type__icontains=query)
            )
        else:
            recipes = self.model.objects.all()
        return recipes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calculate comment count for each post
        for recipe in context["recipes"]:
            recipe.comment_count = recipe.comments.count()
        return context


def RecipeDetail(request, pk):
    """
    View a single recipe
    """

    template_name = "recipes/recipe_detail.html"
    recipe = get_object_or_404(Recipe, pk=pk)
    comments = CommentRecipe.objects.filter(recipe=recipe)
    comments_order = recipe.comments.order_by("-created_on")
    comment_count = recipe.comments.count()
    liked = False

    if recipe.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == "POST":
        comment_form = CommentRecipeForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, "Comment submitted successfully"
            )
            return HttpResponseRedirect(request.path_info)
    else:
        comment_form = CommentRecipeForm()

    return render(
        request,
        template_name,
        {
            "recipe": recipe,
            "liked": liked,
            "comments": comments,
            "comment_form": comment_form,
            "comment_count": comment_count,
            "template_name": template_name,
        },
    )


def LikeView(request, pk):
    """
    Handles the like function. Like and unlike recipes
    """
    recipe = get_object_or_404(Recipe, id=request.POST.get("like_id"))
    liked = False

    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
        liked = False
        messages.add_message(
            request, messages.SUCCESS,
            "You have successfully unliked this post!"
        )

    else:
        recipe.likes.add(request.user)
        liked = True
        messages.add_message(
            request, messages.SUCCESS,
            "You have successfully liked this post!"
        )

    return HttpResponseRedirect(reverse("recipe_detail", args=[str(pk)]))


class AddRecipe(LoginRequiredMixin, CreateView):
    """
    Add recipe view
    """

    template_name = "recipes/add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)


class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit a recipe
    """

    template_name = "recipes/edit_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Detele a recipe
    """

    model = Recipe
    success_url = "/recipes/"

    def test_func(self):
        return self.request.user == self.get_object().user


def comment_edit(request, pk, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        recipe = get_object_or_404(Recipe, pk=pk)
        comments = CommentRecipe.objects.filter(recipe=recipe)
        comment = get_object_or_404(CommentRecipe, pk=comment_id)
        comment_form = CommentRecipeForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.user == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(request, messages.ERROR,
                                 "Error updating comment!")

    return HttpResponseRedirect(reverse("recipe_detail", args=[pk]))


def comment_delete(request, pk, comment_id):
    """
    view to delete comment
    """
    recipe = get_object_or_404(Recipe, pk=pk)
    comment = get_object_or_404(CommentRecipe, pk=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("recipe_detail", args=[pk]))
