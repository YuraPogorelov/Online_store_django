from django.contrib import admin
from .models import Category, Brand, Product, CartItem, Cart

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass