from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from djmoney.models.fields import MoneyField

from products.models import Product


class Cart(models.Model):
    products = models.ManyToManyField(Product, through='CartProductM2M')
    total = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', default=0)

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

    def __str__(self):
        return str(self.total)

    def get_absolute_url(self):
        return reverse('Cart_detail', kwargs={'pk': self.pk})


class CartProductM2M(models.Model):

    class Sizes(models.TextChoices):
        x_small = 'xs', 'XS'
        small = 's', 'S'
        medium = 'm', 'M'
        large = 'l', 'L'
        x_large = 'xl', 'XL'
        xx_large = 'xxl', 'XXL'
        six = 6, 'six'
        seven = 7, 'seven'
        eight = 8, 'eight'
        nine = 9, 'nine'
        ten = 10, 'ten'
        eleven = 11, 'eleven'
        twelve = 12, 'twelve'

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=6, choices=Sizes.choices)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.product.title
