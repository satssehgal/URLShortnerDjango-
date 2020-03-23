from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from django.core import serializers
from django.contrib import messages
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.db import connection
from . models import URLData
from . forms import URLDataForm
from . serializers import URLDataSerializers
from django.shortcuts import redirect
import sqlite3
import string
import random

#Declare Key Varaibles
BASE_LIST='0123456789abcdefghijklmnopqrstuvwxyz./:'
BASE_DICT=dict((c,idx) for idx,c in enumerate(BASE_LIST))
service_url='http://localhost:8001'

class FullURLView(viewsets.ModelViewSet):
	queryset=URLData.objects.all()
	serializers_class=URLDataSerializers

def base_encode(integer, alphabet=BASE_LIST): #Convert ID to FullURL
    if integer == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while integer:
        integer, rem = divmod(integer, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)

def base_decode(request, reverse_base=BASE_DICT): #Convert Full URL to ID
    longurl=request
    length = len(reverse_base)
    ret = 0
    for i, c in enumerate(longurl[::-1]):
        ret += (length ** i) * reverse_base[c]
    return ret

def shortChars(): #Get Shortened URL endpoint
    SHORT_LIST_CHAR='0123456789'+string.ascii_letters
    return ''.join([random.choice(SHORT_LIST_CHAR) for i in range(10)])

def checkIDExists(ID): #Check to see if ID exists in DB
    sc=str(shortChars())
    Retreived_IDs=list(URLData.objects.values_list('URLID', flat=True))
    if str(ID) in Retreived_IDs:
        surl=URL_ID=URLData.objects.all().filter(URLID=str(ID))[0].ShortURL
        mess="Record Already Exists. \n\nLink is: {}/{}".format(service_url,surl)
    else:
        U=URLData(URLID=ID, ShortURL=sc)
        U.save()
        mess=("Your shortened URL is {}/{}".format(service_url,sc))
    return mess

def redirect_short_url(request, short_url):
    redirect_url = service_url+'/shorten'
    try:
        URL_ID=URLData.objects.all().filter(ShortURL=short_url)[0].URLID
        redirect_url = base_encode(int(URL_ID))
    except Exception as e:
        print (e)
    return redirect(redirect_url)       

def get_form(request):
    if request.method=='POST':
        form=URLDataForm(request.POST)
        if form.is_valid():
            fullurl=form.cleaned_data['EnterURL']
            ID=base_decode(fullurl.lower())
            messages.success(request, '{}'.format(checkIDExists(ID)))
    form=URLDataForm()
    return render(request, 'myform/form.html', {'form':form})


