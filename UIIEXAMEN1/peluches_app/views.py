from django.shortcuts import render
from .models import Sucursal
# Create your views here.

def index_vista(request):
    ListaSucursales=Sucursal.objects.all()
    return render (request,'index.html',{'ListaSucursal':ListaSucursales})