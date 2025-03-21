from django.urls import path
from .views import BookListView, BookDetailView, ReviewCreateView, SearchBookView, BookReviewCreateView, AboutMeView

urlpatterns = [
    path('book/', BookListView.as_view(), name='book_list'),  # Список книг
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),  # Детальная страница книги
    path('<int:pk>/review/', ReviewCreateView.as_view(), name='add_review'),  # Добавление отзыва
    path('search/', SearchBookView.as_view(), name='search_book'),
    path('<int:pk>/reviews/', BookReviewCreateView.as_view(), name='book_review_create'),
    path('about_me/', AboutMeView.as_view(), name='about_me'),
]

