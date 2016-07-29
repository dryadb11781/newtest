
# -*- conding:utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
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
def welcome(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('Welcome!~'+request.GET['user_name'])
    else:
        return render_to_response('welcome.html', locals())
