# Generated by Django 5.0.3 on 2024-05-07 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_products_available'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('name',), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]
