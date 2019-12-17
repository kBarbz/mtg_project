from django.shortcuts import render
from .forms import CoinForm, DiceForm
from dice.views import dice_roll, coin_flip
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

# Create your views here.
def random_number(request):

    coin_form = CoinForm()
    dice_form = DiceForm()

    context = {
        "coin_form": coin_form,
        "dice_form": dice_form,
    }
    return render(request, "random_number.html", context)


def home_dice_roll(request):

    coin_form = CoinForm()
    dice_form = DiceForm()

    if request.method == 'POST':
        rolls = int(request.POST.get('rolls'))
        size = int(request.POST.get('size'))
        my_int = dice_roll(request, rolls, size)

        return JsonResponse(my_int, safe=False)

    context = {
        "coin_form": coin_form,
        "dice_form": dice_form,
    }
    return render(request, "random_number.html", context)

def home_coin_flip(request):

    coin_form = CoinForm()
    dice_form = DiceForm()

    if request.method == 'POST':

        flips = int(request.POST.get('flips'))
        thumb = request.POST.get('thumb')
        my_int = coin_flip(request, flips, thumb)
        if thumb == 'false':
            i = 0
            for num in my_int:
                if num == 0:
                    my_int[i] = "Heads"
                    i += 1
                else:
                    my_int[i] = "Tails"
                    i += 1
        else:
            i = 0
            for num in my_int:
                if num == 0:
                    my_int[i] = "Heads/Heads"
                    i += 1
                if num == 1:
                    my_int[i] = "Tails/Tails"
                    i += 1
                if num == 2:
                    my_int[i] = "Tails/Heads"
                    i += 1
                if num == 3:
                    my_int[i] = "Heads/Tails"
                    i += 1
        return JsonResponse(my_int, safe=False)

    context = {
        "coin_form": coin_form,
        "dice_form": dice_form,
    }
    return render(request, "random_number.html", context)
