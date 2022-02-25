from django.shortcuts import render, redirect
from .models import Dojo, Ninja
def index(request):
    context={
        'all_dojos': Dojo.objects.all()
    }
    return render(request,'index.html', context)
def new_dojo(request):
    Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
    return redirect('/')
# Create your views here.
def new_ninja(request):
    Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo=Dojo.objects.get(id=request.POST['dojo']))
    return redirect('/')
def delete_dojo(request, id):
    d= Dojo.objects.get(id=id)
    d.delete()
    return redirect('/')