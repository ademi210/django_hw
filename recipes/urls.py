from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('recipe/<int:pk>/', views.RecipesDetail.as_view(), name='recipes_detail'),
    path('add_ingredient/<int:pk>/', views.IngredientCreateView.as_view(), name='add_ingredient'),
    path('add_recipe/', views.RecipeCreateView.as_view(), name='recipe_create'),

]