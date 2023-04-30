from django.contrib import admin

from products.models import Product, ClothesSize, FootwearSize


class ProductClothesSizesInline(admin.StackedInline):
    model = ClothesSize
    extra = 0


class ProductFootwearSizesInline(admin.StackedInline):
    model = FootwearSize
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    inlines = [
        ProductClothesSizesInline,
        ProductFootwearSizesInline,
    ]


admin.site.register(ClothesSize)
admin.site.register(FootwearSize)
