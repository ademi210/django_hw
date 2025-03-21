from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from .models import Book, Review
from .forms import ReviewForm

class BookListView(generic.ListView):
    model = Book
    template_name = 'book/book.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()
        return context


class BookReviewCreateView(generic.View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        book = get_object_or_404(Book, pk=pk)
        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data['text'],
                star=form.cleaned_data['star'],
                book=book
            )
            return redirect('book_detail', pk=book.pk)
        return HttpResponse('Invalid data')


class AboutMeView(generic.View):
    def get(self, request):
        return HttpResponse("Меня зовут Адэми")


class AboutAnimalView(generic.View):
    def get(self, request):
        return HttpResponse("муя")


class ReviewCreateView(generic.View):
    def post(self, request, id):
        form = ReviewForm(request.POST)
        book = get_object_or_404(Book, id=id)
        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data['text'],
                star=form.cleaned_data['star'],
                book=book
            )
            return redirect('book_detail', id=id)
        return render(request, 'book/book_detail.html', {'book': book, 'form': form})

class SearchBookView(generic.ListView):
    template_name = 'book/search_results.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Book.objects.filter(title__icontains=query)
        return Book.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context