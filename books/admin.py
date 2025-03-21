from django.contrib import admin
from .models import Book, Review


@admin.register(Book)
class Book(admin.ModelAdmin):
    list_display = ('title', 'price', 'genre',  'author')
    list_filter = ('genre', 'author')
    search_fields = ('title', 'genre', 'author')


admin.site.register(Review)
