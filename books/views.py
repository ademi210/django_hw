from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Review
from .forms import ReviewForm
from django.shortcuts import redirect




def book_list_view(request):
    if request.method == 'GET':
        books = Book.objects.all()
        return render(request, 'book/book.html', {'books': books})


def book_detail_view(request, id):
    if request.method == 'GET':
        form = ReviewForm()
        book = Book.objects.get(id=id)
        return render(request, 'book/book_detail.html', {'book': book, 'form': form})
    elif request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data['text'],
                star=form.cleaned_data['star'],
                book=Book.objects.get(id=id)
            )
            return redirect('book_detail', id=id)
        else:
            return HttpResponse('Invalid data')



def about_me(request):
    if request.method == "GET":
        return HttpResponse("kmkm")


def about_animal(request):
    if request.method == "GET":
        return HttpResponse("<h1> У меня есть домашнее животное. Кошка. ее зовут Кэтти. "
                            "Увидеть ее можно по ссылке image/ </h1>")


