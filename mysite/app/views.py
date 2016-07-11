
# -*- conding:utf-8 -*-
from django.http import HttpResponse
from django import template
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext


def here(request):
    return HttpResponse('中文!')
def math(request, a, b):
    a = int(a)
    b = int(b)
    s = a + b
    d = a - b
    p = a * b
    q = a / b
    return  render_to_response('math.html',{'s':s, 'd':d, 'p':p, 'q':q},
    )
def menu(request):
    food0 = {'name': 'hamburger', 'price': 100, 'comment': '好吃','is_spicy': False}
    food1 = {'name': 'chicken', 'price': 200, 'comment': '超人氣','is_spicy': True}
    foods = [food0,food1]

    return render_to_response('menu.html',locals())
