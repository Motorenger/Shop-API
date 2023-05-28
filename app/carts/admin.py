from django.contrib import admin

from carts.models import Cart, CartProductM2M


class CartProductInline(admin.TabularInline):
    model = Cart.products.through


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartProductInline]


admin.site.register(CartProductM2M)
