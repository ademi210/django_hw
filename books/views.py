from django.utils import timezone
from django.views.generic import DetailView, ListView
from . import models
from django.http import HttpResponse
from django.views import View
from .models import Book


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'


class BookListView(ListView):
    model = Book
    template_name = 'book/book.html'
    context_object_name = 'books'


class AboutMeView(View):
    def get(self, request):
        return HttpResponse("Меня зовут адэми, мне 20 лет")


class FavoriteAnimalView(View):
    def get(self, request):
        return HttpResponse(
            "Моё любимое животное кошка. Я люблю кошек за их грациозность и красоту, "
            "и ещё за их ловкость и быстроту. Кошки очень любят спать и играть. "
            "Кошки с мягкой шерстью, с красивыми и блестящими глазами и мощными лапами."
            "<''>"
        )

class SystemTimeView(View):
    def get(self, request):
        now = timezone.now()
        return HttpResponse(f'Текущее время {now}')



class BookSearchView(ListView):
    model = Book
    template_name = 'book/book_search.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Book.objects.filter(title__icontains=query)
        return Book.objects.all()
