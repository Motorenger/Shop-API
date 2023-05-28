# Generated by Django 4.2 on 2023-05-01 20:29

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("carts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="total",
            field=djmoney.models.fields.MoneyField(
                decimal_places=2,
                default=Decimal("0"),
                default_currency="USD",
                max_digits=10,
            ),
        ),
    ]
