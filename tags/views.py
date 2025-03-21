from django.shortcuts import render
from .models import Product

def all_category_book(request):
    if request.method == 'GET':
        books = Product.objects.all()
        return render(request, 'tags/all_category_book.html', {'all_category_books': books})

def children_books(request):
    books = Product.objects.filter(category='Книги для детей')
    return render(request, 'tags/children_books.html', {'children_books': books})

def teen_books(request):
    books = Product.objects.filter(category='Книги для подростков')
    return render(request, 'tags/teen_books.html', {'teen_books': books})