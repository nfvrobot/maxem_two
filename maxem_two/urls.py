from django.urls import path
from . import views

urlpatterns = [
    path('home-page/', views.home_page, name='home_page'),
    path('home-page/details/<int:id>', views.details, name='details'),
]
