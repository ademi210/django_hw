# Generated by Django 5.1.7 on 2025-03-21 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]
