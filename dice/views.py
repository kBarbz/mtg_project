from django.shortcuts import render
from random import randint
from .forms import CoinForm, DiceForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

# Create your views here.
def dice_roll(request, n, s):
    my_int = []
    while n > 0:
        my_int.append(randint(1,s))
        n -= 1
    return my_int

def coin_flip(request, n, thumb):
    my_int = []
    if thumb == 'false':
        while n > 0:
            my_int.append(randint(0,1))
            n -= 1
    else:
        while n > 0:
            my_int.append(randint(0,3))
            n -= 1
    return my_int

def home_dice_roll(request):

    coin_form = CoinForm()
    dice_form = DiceForm()


    rolls = int(request.POST.get('rolls'))
    size = int(request.POST.get('size'))
    my_int = dice_roll(request, rolls, size)

    return JsonResponse(my_int, safe=False)


def home_coin_flip(request):

    coin_form = CoinForm()
    dice_form = DiceForm()

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
