# Generated by Django 5.1.7 on 2025-03-25 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mangamodel',
            name='title',
        ),
        migrations.AddField(
            model_name='mangamodel',
            name='rating',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
