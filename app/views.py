from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    ETFDO=Topic_form()
    d={'ETFDO':ETFDO}

    if request.method=='POST':
        TFDO=Topic_form(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()

            QLTO=Topic.objects.all()
            d={'QLTO':QLTO}

            return render(request,'display_topic.html',d)
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFDO=Webpage_form()      
    d={'EWFDO':EWFDO}

    if request.method=='POST':
        WFDO=Webpage_form(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']# it has primary key not the name (for backend pk will go but for us it displays topic name)
            n=WFDO.cleaned_data['name']
            u=WFDO.cleaned_data['url']
            e=WFDO.cleaned_data['email']
            re= WFDO.cleaned_data['re_enter_email']
            TO=Topic.objects.get(topic_name=tn)#since we cannot insert data through pk as tn contains pk, so we will convert get the entire object with the help of pk
            WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]#Now we will use the object where it contains all the data which includes topic_name
            WO.save()

            QLWO=Webpage.objects.all()
            d={'QLWO':QLWO}

            return render(request,'display_webpage.html',d)
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    EAFDO=AccessRecord_form()
    d={'EAFDO':EAFDO}

    if request.method=='POST':
        AFDO=AccessRecord_form(request.POST)
        if AFDO.is_valid():
            n=AFDO.cleaned_data['name']
            d=AFDO.cleaned_data['date']
            a=AFDO.cleaned_data['author']
            wo=Webpage.objects.get(pk=n)
            AO=AccessRecord.objects.get_or_create(name=wo,date=d,author=a)[0]
            AO.save()
            QLAO=AccessRecord.objects.all()
            d={'QLAO':QLAO}
            return render(request,'display_accessrecord.html',d)
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_accessrecord.html',d)


def display_webpage(request):
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)


def display_accessrecord(request):
    QLAO=AccessRecord.objects.all()
    d={'QLAO':QLAO}
    return render(request,'display_accessrecord.html',d)

def display_topic(request):
    QLTO=Topic.object.all()
    d={'QLTO':QLTO}
    return render(request,'display_topic.html',d)





        

    






        
