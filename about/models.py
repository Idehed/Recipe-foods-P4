from django.db import models


class About(models.Model):
    """
    model for creating and storing about me text
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
