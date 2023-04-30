from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from djmoney.models.fields import MoneyField


class Product(models.Model):

    class ProductTypes(models.TextChoices):
        clothes = 'clothes', _('Clothes')
        footwear = 'footwear', _('Footwear')

    title = models.CharField(max_length=255)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')

    type = models.CharField(max_length=8, choices=ProductTypes.choices)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.title

    def retrieve_url(self):
        return reverse("products:retrieve", kwargs={"pk": self.pk})


class ClothesSize(models.Model):
    class Sizes(models.TextChoices):
        x_small = 'xs', 'XS'
        small = 's', 'S'
        medium = 'm', 'M'
        large = 'l', 'L'
        x_large = 'xl', 'XL'
        xx_large = 'xxl', 'XXL'

    size = models.CharField(max_length=4, choices=Sizes.choices)
    product = models.ForeignKey(Product, related_name='clothes_sizes', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.size


class FootwearSize(models.Model):
    class Sizes(models.IntegerChoices):
        six = 6
        seven = 7
        eight = 8
        nine = 9
        ten = 10
        eleven = 11
        twelve = 12

    size = models.IntegerField(choices=Sizes.choices)
    product = models.ForeignKey(Product, related_name='footwear_sizes', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.size)
