from django.urls import path
from . import views



app_name = 'mymeals'

urlpatterns = [
    path('', views.meals_list, name='product_list'),
    path('<slug:slug>', views.meals_details , name='products_details'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    path('contact/', views.conntact, name='contact'),
]
