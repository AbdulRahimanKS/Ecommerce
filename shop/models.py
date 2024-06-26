from django.db import models
from django.template.defaultfilters import slugify
from django.shortcuts import get_object_or_404
from django.urls import reverse

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('prodcat', args =[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class products(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='products')
    desc = models.TextField()
    stock = models.IntegerField()
    price = models.IntegerField()
    available = models.BooleanField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('prod-detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name
