from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=225, verbose_name='نام دسته بندی')
    url_slug = models.CharField(max_length=80, verbose_name='عنوان در یو ار ال')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'کتگوری'
        verbose_name_plural = 'کتگوری ها'


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=225, verbose_name='نام کالا')
    url_slug = models.CharField(max_length=80, verbose_name='عنوان در یو ار ال')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    price = models.FloatField(verbose_name='قیمت')
    image = models.ImageField(upload_to='item_images', null=True, blank=True)
    is_sold = models.BooleanField(verbose_name='فروخته شده؟')
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'کالا'
        verbose_name_plural = 'کالا ها'

