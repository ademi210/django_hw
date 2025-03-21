from django.views.generic import ListView
from .models import Product




class AllCategoryBookView(ListView):
    model = Product
    template_name = 'tags/all_category_book.html'
    context_object_name = 'all_category_books'

    def get_queryset(self):
        return Product.objects.all()


class ChildrenBooksView(ListView):
    model = Product
    template_name = 'tags/children_books.html'
    context_object_name = 'children_books'

    def get_queryset(self):
        return Product.objects.filter(category='Книги для детей')


class TeenBooksView(ListView):
    model = Product
    template_name = 'tags/teen_books.html'
    context_object_name = 'teen_books'

    def get_queryset(self):
        return Product.objects.filter(category='Книги для подростков')
