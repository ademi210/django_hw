from django.shortcuts import  render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .forms import IngredientForm, RecipeForm
from recipes.models import Recipe, Ingredient
from django.urls import reverse_lazy


class HomePage(ListView):
    model = Recipe
    template_name = 'rs/recipes.html'
    context_object_name = 'recipes'

class RecipesDetail(DetailView):
    model = Recipe
    template_name = 'rs/recipe_detail.html'
    context_object_name = 'recipes'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Recipe, pk=pk)

class IngredientCreateView(CreateView):
    model = Ingredient
    template_name = 'recipes/add_ingredient.html'
    form_class = IngredientForm

    def form_valid(self, form):
        form.instance.recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        form.save()
        return redirect('recipe_detail', pk=self.kwargs['pk'])

class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'recipes/add_recipe.html'
    form_class = RecipeForm
    success_url = reverse_lazy('recipe_list')




