from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

MEAL_TYPES = (
    ("breakfast", "Breakfast"),
    ("lunch", "Lunch"),
    ("dinner", "Dinner"),
    ("snacks", "Snacks"),
)


class Recipe(models.Model):
    """
    Model to create and manage recipes
    """

    user = models.ForeignKey(
        User, related_name="recipe_owner", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    instructions = RichTextField(max_length=10000, null=False, blank=False)
    ingredients = RichTextField(max_length=10000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="recipes/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_description = models.CharField(max_length=150, null=False, blank=False)
    meal_type = models.CharField(max_length=50, choices=MEAL_TYPES, default="breakfast")
    calories = models.IntegerField()
    posted_date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="liked_recipes")

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return str(self.title)


class CommentRecipe(models.Model):
    """
    Model for the comment section in the detailed recipe view
    """

    recipe = models.ForeignKey(
        Recipe, related_name="comments", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, related_name="commenter", on_delete=models.CASCADE)

    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.user}"
