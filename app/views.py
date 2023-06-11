from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def student(request):
    sof=Studentform()
    d={'sof':sof}
    if request.method=='POST':
        SD=Studentform(request.POST)
        if SD.is_valid():
            return HttpResponse(str(SD.cleaned_data))
        return HttpResponse('data submited successfull..!')

    return render(request,'student.html',d)

def display_data(request):
    sot=Studentform()
    d1={'sot':sot}
    return render(request,'display_data.html',d1)