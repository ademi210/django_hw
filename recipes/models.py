from django.db import models
from django.template.defaultfilters import title


class Recipe(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=500)
    quantity = models.PositiveIntegerField(default=0)
    recipe = models.ManyToManyField(Recipe, related_name='ingredients')

    def __str__(self):
        return self.name