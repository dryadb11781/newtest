#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from restaurants.models import Restaurant, Food,Comment
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.template import RequestContext
# Create your views here.
def menu(request,id):
    if id:
    #path = request.path
        restaurant = Restaurant.objects.get(id=id)
        return render_to_response('menu.html',locals())
    else:
        return HttpResponseRedirect("/restaurants_list")
def meta(request):
    values = request.META.items()

    sorted(values)
    html = []
    for k, v in values:
        html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v))
        return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))
def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render_to_response('restaurants_list.html',locals())

def comment(request, restaurant_id):
    
    if restaurant_id:
        r = Restaurant.objects.get(id=restaurant_id)
    else:
        return HttpResponseRedirect("/restaurants_list/")
    if request.POST:
        visitor = request.POST['visitor']
        content = request.POST['content']
        email = request.POST['email']
        date_time = timezone.localtime(timezone.now())
        Comment.objects.create(
            visitor=visitor, email=email,
            content=content,
            date_time=date_time,
            restaurant=r
        )
    return render_to_response('comments.html', RequestContext(request, locals()))
