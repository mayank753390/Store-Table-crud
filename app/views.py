from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def insert_topic(request):
    tn=input('Enter Topic name')
    TOD=Topic.objects.get_or_create(topic_name=tn)
    if TOD[1]:
        return HttpResponse('New Topic is Created')
    else:
        return HttpResponse('Given Topic is Already Present')
    
def insert_webpage(request):
    tn=input('Enter Topic name')
    n=input('Enter Name')
    url=input('Enter Url')
    email=input('Enter Email')
    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        WTOD=Webpage.objects.get_or_create(topic_name=LTO[0],name=n,url=url,email=email)
        if WTOD[1]:
            return HttpResponse('Web Is Created')
        else:
            return HttpResponse('Web is Presented')
    else:
        return HttpResponse('Given Topic is Not Present')    
def insert_accessRecordss(request):

    pk=int(input('Enter pk of Webpage'))
    author=input('Enter author')
    date=input('enter date') 

    LWO = Webpage.objects.filter(pk=pk)

    if LWO:
        WO = LWO[0]
        ATOD = AccessRecords.objects.get_or_create(webpage=WO, author=author, date=date)    

        
        if ATOD[1]:
            return HttpResponse('New Access is Created')
        else:
            return HttpResponse('With Given Details Acess is already Present')
    else:
        return HttpResponse('Given Present Webpage Table Data is Not Present in DB') 


def display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topic.html',d)        
    
