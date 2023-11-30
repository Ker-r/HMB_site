from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(
        'Название категории товара',
        max_length=200
    )
    slug = models.SlugField(
        'Название ссылки',
        unique=True
    )

    def _str_(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(
        'Название товара',
        max_length=200
    )
    description = models.TextField(
        'Описание товара'
    )
    price = models.IntegerField(
        'Цена товара'
    )
    category = models.ForeignKey(
        verbose_name='Категория',
        to='Category',
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name='product'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    image = models.ImageField(
        'Картинка',
        upload_to='product/',
        blank=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop_detail', kwargs={'shop_pk': self.pk})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
