from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    dtmus = {
        'nickname':"Music",
        'Age':17,
        'fav':['soft bear','soft doll']
    }
    return HttpResponse(template.render(dtmus,request))  
