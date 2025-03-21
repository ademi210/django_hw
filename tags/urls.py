from django.urls import path
from . import views

urlpatterns = [
    path('all_category_book/', views.all_category_book, name='all_category_book'),
    path('children_books/', views.children_books, name='children_books'),
    path('teen_books/', views.teen_books, name='teen_books'),
]