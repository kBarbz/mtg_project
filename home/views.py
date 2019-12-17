from django.shortcuts import render
from dice.forms import CoinForm, DiceForm
from dice.views import dice_roll, coin_flip
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from dice.views import home_coin_flip, home_dice_roll

# Create your views here.
def home(request):

    coin_form = CoinForm()
    dice_form = DiceForm()

    context = {
        "coin_form": coin_form,
        "dice_form": dice_form,
    }
    return render(request, "home.html", context)
