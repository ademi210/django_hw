from django.urls import path
from . import views


urlpatterns = [
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('about_me/', views.AboutMeView.as_view(), name='about_me'),
    path('favorite_animal/', views.FavoriteAnimalView.as_view(), name='favorite_animal'),
    path('system_time/', views.SystemTimeView.as_view(), name='system_time'),
    path('search/', views.BookSearchView.as_view(), name='book_search'),
]
