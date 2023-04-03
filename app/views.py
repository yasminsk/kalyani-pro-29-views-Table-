from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def insert_Topic(request):
    tn=input('enter topic_name')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()
    return HttpResponse('Topic is inserted successfull')

def insert_Webpage(request):
    tn=input('enter topic_name')
    n=input('enter name')
    url=input('enter url')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()
    Wo=Webpage.objects.get_or_create(topic_name=To,name=n,url=url)[0]
    Wo.save()
    return HttpResponse('Webpage is inserted')

def insert_AccessRecord(request):
    tn=input('enter topic_name')
    n=input('enter name')
    url=input('enter url')
    a=input('enter author')
    d=input('enter date')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()
    Wo=Webpage.objects.get_or_create(topic_name=To,name=n,url=url)[0]
    Wo.save()
    Ao=AccessRecord.objects.get_or_create(name=Wo,author=a,date=d)[0]
    Ao.save()
    return HttpResponse('AccessRecord is inserted')