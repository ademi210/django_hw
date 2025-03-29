from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from django.views import View
from .models import Book
from django.core.cache import cache
from django.views.decorators.cache import cache_page


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'

@method_decorator(cache_page(60*15), name='dispatch')
class BookListView(ListView):
    model = Book
    template_name = 'book/book.html'
    context_object_name = 'books'

    def get_queryset(self):
        books = cache.get('books')
        if not books:
            books = self.model.objects.all()
            cache.set('books', books)
        return books


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
