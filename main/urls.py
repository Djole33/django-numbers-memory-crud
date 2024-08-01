from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="index"),
   path('numbers-list/', views.numbers_view, name="numbers-list"),
   path('recall/', views.guess_view, name="recall"),
   path('delete-guess/', views.delete_guess, name="delete-guess"),
   path('results/', views.results, name="results"),
]
