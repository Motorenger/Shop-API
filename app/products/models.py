from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from djmoney.models.fields import MoneyField


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.title

    def retrieve_url(self):
        return reverse("products:retrieve", kwargs={"pk": self.pk})
