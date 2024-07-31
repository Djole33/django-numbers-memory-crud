from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="index"),
   path('numbers-list/', views.numbers_view, name="numbers-list"),
]
