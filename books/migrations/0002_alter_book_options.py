# Generated by Django 5.1.7 on 2025-03-21 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книгу', 'verbose_name_plural': 'Книги'},
        ),
    ]
