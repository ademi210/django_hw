from django.urls import path
from . import views

urlpatterns = [
    path('all_category_books/', views.AllCategoryBookView.as_view(), name='all_category_books'),
    path('children_books/', views.ChildrenBooksView.as_view(), name='children_books'),
    path('teen_books/', views.TeenBooksView.as_view(), name='teen_books'),
]
