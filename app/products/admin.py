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
    list_display = ("title", "type", "price", "in_stock")
    list_filter = ("type", "price", "in_stock")
    search_fields = ("title",)
    inlines = [
        ProductClothesSizesInline,
        ProductFootwearSizesInline,
    ]


admin.site.register(ClothesSize)
admin.site.register(FootwearSize)
