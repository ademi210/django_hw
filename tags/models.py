from django.db import models

class Tag(models.Model):
        CATEGORY_CHOICES = [
            ('children', 'Книги для детей'),
            ('teen', 'Книги для подростков'),
        ]
        name = models.CharField(max_length=100)


        def __str__(self):
            return self.name

        class Meta:
            verbose_name = 'Тег'
            verbose_name_plural = 'Теги'


class Product(models.Model):
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, related_name='products')
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'