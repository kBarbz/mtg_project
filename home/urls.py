from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home_dice_roll", views.home_dice_roll, name="home_dice_roll"),
    path("home_coin_flip", views.home_coin_flip, name="home_coin_flip")
]
