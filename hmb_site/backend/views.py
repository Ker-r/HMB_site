from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


# Стартовая страница
def home(request):
    ''' Главная страница '''
    return render(request, 'hmb_site/home.html')


# def shop(request):
#     return render(request, 'hmb_site/shop.html')


class ShopView(ListView):
    ''' Страница проектов '''
    template_name = 'hmb_site/shop.html'
    model = Product
    context_object_name = 'shop'
