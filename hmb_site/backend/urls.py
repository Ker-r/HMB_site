from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.shop_list, name='shop_list'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('shop/<int:shop_pk>/', views.ShopDetail.as_view(), name='shop_detail'),
]
