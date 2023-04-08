import os
from decimal import Decimal
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

CATEGORY_IMAGES_PATH = os.path.join("uploads", "shop", "category")
PRODUCTS_IMAGES_PATH = os.path.join("uploads", "shop", "products")


# Create your models here.

def category_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.slug, ext)
    return os.path.join(CATEGORY_IMAGES_PATH, filename)


def product_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.slug, instance.category.slug, ext)
    return os.path.join(PRODUCTS_IMAGES_PATH, filename)


def product_secondary_image_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.product.slug, ext)
    return os.path.join(PRODUCTS_IMAGES_PATH, filename)


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to=category_file_name,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(
        upload_to=product_file_name,
        blank=True,
        null=True,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    additional_info = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    tags = TaggableManager()

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_discount(self, rate=25):
        return "%.2f" % (self.price * Decimal((100 + rate) / 100))


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(
        upload_to=product_secondary_image_name,
        blank=False,
        null=False,
    )


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    review = models.TextField()
