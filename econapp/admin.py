from django.contrib import admin
from .models import Category, Brand

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass