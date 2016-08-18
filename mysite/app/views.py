
# -*- conding:utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.contrib import auth


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

def set_cookie(request):
    response = HttpResponse('Set your lucky_number as 8')
    response.set_cookie('lucky_number', 8)
    return response

def get_cookie(request):
    if 'lucky_number' in request.COOKIES:
        return HttpResponse('Your lucky_number is {0}'.format(request.COOKIES['lucky_number']))
    else:
        return HttpResponse('NO cookies.')
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html',RequestContext(request, locals()))



def index(request):
    """index page
    :request: client request
    :returns: index webpage
    """
    return render_to_response('index.html', RequestContext(request, locals()))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')
