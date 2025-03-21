from django.db import models


class Book(models.Model):
    GENRE = (
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
    )
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE)
    email = models.EmailField(null=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'


class Review(models.Model):
    text = models.TextField()
    star = models.PositiveIntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'