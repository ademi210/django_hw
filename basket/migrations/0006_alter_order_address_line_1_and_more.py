# Generated by Django 5.1.7 on 2025-03-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0005_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address_line_1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
