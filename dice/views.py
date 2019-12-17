from django.shortcuts import render
from random import randint

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
