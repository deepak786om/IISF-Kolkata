from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,TemplateView
from . import forms
import requests
import json 
from .models import Rain,DamWaterDay,DamWaterYear,RoadSubmergenceDay,RoadSubmergenceYear
from graphos.renderers.gchart import LineChart
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from . import serializers
from . import models
from. import permissions
import zerosms




# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


def rain(request):
    data_list = Rain.objects.all()
    data_dict = {'rain':data_list}
    return render(request,'test.html',context=data_dict)

def damyear(request):
    data_list = DamWaterYear.objects.all()
    data_dict = {'damyear':data_list}
    return render(request,'dam-discharge-year.html',context=data_dict)

def damday(request):
    data_list = DamWaterDay.objects.all()
    data_dict = {'damday':data_list}
    return render(request,'dam-discharge-15.html',context=data_dict)

def roadsubyear(request):
    data_list = RoadSubmergenceYear.objects.all()
    data_dict = {'roadsubyear':data_list}
    return render(request,'road-sub-year.html',context=data_dict)

def roadsubday(request):
    data_list = RoadSubmergenceDay.objects.all()
    data_dict = {'roadsubday':data_list}
    return render(request,'road-sub-day.html',context=data_dict)

class ThanksPage(TemplateView):
    template_name='thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'

class LoadPage(TemplateView):
    template_name='load.html'

class MailPage(TemplateView):
    template_name='mail.html'



class UserProfileViewset(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset= models.User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfiles,)

class LoginViewSet(viewsets.ViewSet):

    serializer_class=AuthTokenSerializer

    def create(self, request):

        return ObtainAuthToken().post(request)

def sms(request):
    if "sendto" in request.POST:

        sendto=request.POST["sendto"]

        zerosms.sms(phno='6388384317', passwd='7891688909' , receivernum=sendto, message="Alert:Please look for your safety ,your nearest roads will submerge soon.")
        return render(request,"sms.html")
    return HttpResponse(render(request,"sms.html",{}))


def geoip(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('http://api.ipstack.com/117.55.241.53?access_key=e4e71b6fb15607a64c5f5b75856be82a')
#    response = requests.get('http://api.ipstack.com/' + ip_address,params={'access_key': 'e4e71b6fb15607a64c5f5b75856be82a'},)

    geodata = response.text
    print(response.text)
    geodata = json.loads(geodata)
    return render(request, 'geoip.html', {
        'ip': geodata['ip'],
        'city':geodata['city'],
        'country': geodata['country_name'],
	'latitude': '13.0478221',
       # 'latitude': geodata['latitude'],
        # 'longitude': geodata['longitude'],
	'longitude': '80.0685824',
        'api_key': 'e4e71b6fb15607a64c5f5b75856be82a'
    })
