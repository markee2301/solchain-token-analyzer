from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('select-website/', views.select_website, name='select_website'),
    path('redirect/<str:website>/<str:contract_address>/', views.redirect_to_website, name='redirect_to_website'),
]
