
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
