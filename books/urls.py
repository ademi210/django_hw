from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me),
    path('books_list/', views.book_list_view, name='book_list'),
    path('books/<int:id>/', views.book_detail_view, name='book_detail'),
    path('about_animal/', views.about_animal)

]