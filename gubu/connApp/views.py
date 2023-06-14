from django.shortcuts import render

# Create your views here.
from .models import MyPharmacy

# Create your views here.

def home(request):
    m=MyPharmacy.objects.all() #select * from table
    header='Your search for the perfect match is here!'
    header2='Find your special one'
    #client=myclient.objects.all()
    h=[header,header2]
    
    return render(request,'index.html',{'m':m})