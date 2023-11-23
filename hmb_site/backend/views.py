from django.shortcuts import render
# from .models import Product


# Стартовая страница
def home(request):
    ''' Главная страница '''
    return render(request, 'hmb_site/home.html')



