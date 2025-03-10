from django.shortcuts import render
from django.http import HttpResponse
import datetime


def about_me(request):
    if request.method == "GET":
        return HttpResponse("меня зовут адэми, мне 20 лет")


def favorite_animal(request):
    if request.method == "GET":
        return HttpResponse("Моё любимое животное кошка.Я люблю кошек за их грациозность и красоту,и ещё за их ловкость и быстроту.Кошки очень любят спать и играть.Кошки с мягкой шерстью,с красивыми и блестящими глазами и мощными лапами."
                            "<img src='data:image/jpeg;base64,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'>")

def system_time(request):
    if request.method == "GET":
        now = datetime.datetime.now()
        return HttpResponse(f'текущее время {now}')
