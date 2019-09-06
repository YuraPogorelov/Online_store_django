from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Brand(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)

class ProductManager(models.Manager):

    def all(self, *args, **kwargs):
        return super(ProductManager, self).get_queryset().filter(available=True)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to=image_folder)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    available = models.BooleanField(default=True)
    objects = ProductManager()
    
    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"product_slug": self.slug})
    

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'