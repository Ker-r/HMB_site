from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'title', 'price', 'category',)
    # Добавляем интерфейс для поиска по названию и по типу товара
    search_fields = ('title', 'category', )
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка
    empty_value_display = '-пусто-'


class CategoryAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'title', 'slug', )
    # Добавляем интерфейс для поиска по названию и по типу товара
    search_fields = ('title', )
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка
    empty_value_display = '-пусто-'


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)