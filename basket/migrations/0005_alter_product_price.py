# Generated by Django 5.1.7 on 2025-03-21 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0004_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
