from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Product, Category


# Стартовая страница
def home(request):
    ''' Главная страница '''
    return render(request, 'hmb_site/home.html')


# def shop(request):
#     return render(request, 'hmb_site/shop.html')


class ShopView(ListView):
    ''' Страница товаров '''
    template_name = 'hmb_site/shop.html'
    model = Product
    context_object_name = 'shop'


class ShopDetail(DetailView):
    ''' Страница отдельного проекта '''
    model = Product
    template_name = 'hmb_site/shop_detail.html'
    context_object_name = 'shop'
    pk_url_kwarg = 'shop_pk'


# Функция get_object_or_404 получает по заданным критериям объект
# из базы данных или возвращает сообщение об ошибке, если объект не найден.
# В нашем случае в переменную group будут переданы объекты модели Category,
# поле slug у которых соответствует значению slug в запросе
def shop_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Product.objects.filter(category=category)
    context = {
        'category': category,
        'posts': posts
    }

    return render(request, 'hmb_site/shop_list.html', context)
