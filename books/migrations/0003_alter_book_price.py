# Generated by Django 5.1.7 on 2025-03-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_price_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
