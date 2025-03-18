# Generated by Django 5.1.7 on 2025-03-14 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('grade', models.CharField(choices=[('👍', '👍'), ('👍👍', '👍👍'), ('👍👍👍', '👍👍👍'), ('👍👍👍👍', '👍👍👍👍'), ('👍👍👍👍👍', '👍👍👍👍👍')], default=2, max_length=10)),
                ('choice_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='books.book')),
            ],
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]
