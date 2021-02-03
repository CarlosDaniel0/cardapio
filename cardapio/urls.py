from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contato'),
    path('sobre/', views.sobre, name='sobre'),
    path('produto/<int:id>', views.lanche, name='lache'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('carrinho/add/', views.carrinho_add, name='carrinho_add'),
    path('carrinho/remove/', views.carrinho_remove, name='carrinho_remove'),
    path('carrinho/quantidade/', views.carrinho_quantidade, name='carrinho_quantidade'),
]

