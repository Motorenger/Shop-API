# Generated by Django 4.2 on 2023-04-30 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_clothessize_product_footwearsize'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=False),
        ),
    ]