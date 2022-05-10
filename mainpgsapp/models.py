from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='name', max_length=64, unique=True)
    description = models.TextField(verbose_name='description', blank=True)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='name', max_length=128, unique=True)
    image = models.ImageField(upload_to='products_img', blank=True)
    price = models.DecimalField(verbose_name='Price', max_digits=8, decimal_places=2, default=0)
    short_desc = models.TextField(verbose_name='short_desc', blank=True, max_length=300)
    description = models.TextField(verbose_name='description', blank=True)
    quantity = models.PositiveIntegerField(verbose_name='quantity in warehouse', default=0)

    def __str__(self):
        return f'{self.name} - {self.category.name}'


