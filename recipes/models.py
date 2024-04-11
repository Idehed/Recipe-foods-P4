from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

class Recipe(models.Model):
    """
    Model to create and manage recipes
    """
    user = models.ForeingKey(user, related_name='recipe_owner', on_delete=models.CASCADE)
    title = models.CharField(max_lenght=300, null=False, blank=False)
    description = models.CharField(max_lenght=500, null=False, blank=False)
    instructions = models.RichTextField(max_lenght=10000, null=False, blank=False)
    ingredients = models.RichTextField(max_lenght=10000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None], quality=75, upload_to='recipes/', force_format='WEBP',
        blank=False, null=False
    )
    image_description = models.Charfield(max_lenght=150, null=False, blank=False)
    meal_type = models.Charfield(max_lenght=50, choices=MEAL_TYPES, default='breakfast')
    calories = models.IntergerField()
    posted_date = models.DateTimeField(auto_now=True,)

    class Meta:
        ordering = [-'posted_date']

    def __str__(self):
        return str(self.title)
