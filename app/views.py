from django.shortcuts import render
from django.db.models.functions import Length

# Create your views here.
from django.http import HttpResponse
from app.models import *
def insert_topic(request):
    tn=input('Enter Topic name')
    TOD=Topic.objects.get_or_create(topic_name=tn)
    if TOD[1]:
        LTO=Topic.objects.all()
        d={'LTO':LTO}
        return render(request,'display_topic.html',d) 
        #return HttpResponse('New Topic is Created')
    else:
        return HttpResponse('Given Topic is Already Present')
    
    
def insert_webpage(request):
    tn=input('Enter Topic name')
    n=input('Enter Name')
    url=input('Enter Url')
    email=input('Enter Email')
    WTO=Topic.objects.filter(topic_name=tn)
    if WTO:
        WTOD=Webpage.objects.get_or_create(topic_name=WTO[0],name=n,url=url,email=email)
        if WTOD[1]:
            WTO=Webpage.objects.all()
            d={'WTO':WTO}
            return render (request,'display_webpage.html',d)      

            #return HttpResponse('Web Is Created')
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

def display_webpage(request):
    WTO=Webpage.objects.all()
    #WTO=Webpage.objects.all().order_by('name')
    #WTO=Webpage.objects.all()[0:3:1]
    #WTO=Webpage.objects.all().order_by('-name')
    #WTO=Webpage.objects.all().order_by(Length('name'))

    #WTO=Webpage.objects.all().order_by(Length('name').desc())

    #WTO=Webpage.objects.filter(name__startswith='m')

   # WTO=Webpage.objects.filter(name__endswith='n')

   # WTO=Webpage.objects.filter(name__contains='n')



    



    d={'WTO':WTO}
    return render (request,'display_webpage.html',d)  

def display_AccessRecords(request):
    ATO=AccessRecords.objects.all()
    #ATO=AccessRecords.objects.filter(date__year='2025')
    
    #ATO=AccessRecords.objects.filter(date__month='12')

    #ATO=AccessRecords.objects.filter(date__day='06')

   # ATO=AccessRecords.objects.filter(date='2025-06-15')


    d={'ATO':ATO}
    return render(request,'Access_Records.html',d)

def update_Webpage(request):
    #WTO=Webpage.objects.all()

   # Webpage.objects.filter(name='Munna bhaiya').update(topic='Cricket')
    Webpage.objects.filter(url='http://rohit.com').update(topic='Chess',name='Don')

    WTO=Webpage.objects.all()
    
    d={'WTO':WTO}
    return render (request,'display_webpage.html',d)  



def delete_webpage(request):
    WTO= Webpage.objects.filter(name='Raman').delete()

    WTO=Webpage.objects.all()



    d={'WTO':WTO}
    return render (request,'display_webpage.html',d)

def delete_Book(request):
    #BKO=Book.objects.filter(name='Advance Python').delete()
   # BKO=Book.objects.filter(name='HTML').delete()
    #BKO=Book.objects.filter(Name='CSS')
    BKO=Book.objects.filter(Name='PYTHON').all()



    d={'BKO':BKO}
    return render(request,'delete_Book.html',d)



def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        tn = request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        email=request.POST['email']
        To=Topic.objects.get(topic_name=tn)

        WBO=Webpage.objects.get_or_create(topic=To,name=name,url=url,email=email)
        if WBO[1]:
            return HttpResponse(f'{name} object is created')
        else:
            return HttpResponse(f'{name} object is already Present')
        
    return render(request,'insertdata_Form.html',d)  


def select_multiple(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        Itns=request.POST.getlist('tns')

        WEQS=Webpage.objects.none()
        for tn in Itns:
            WEQS=WEQS|Webpage.objects.filter(topic=tn)
        d1={'WTO':WEQS}
        return render(request,'display_webpage.html',d1)



    return render(request,'select_multipe.html',d)          



