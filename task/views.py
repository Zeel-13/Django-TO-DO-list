from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        data=request.POST
        t=data.get('title')
        if t=="":
            messages.info(request,"invalid title")
            return redirect('/')
        user=Task.objects.create(
            title=t
        )
        user.save()
        return redirect('/')
    queryset=Task.objects.all()
    context={'queryset':queryset}
    return render(request,'index.html',context)

def update(request,id):
    user=Task.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        t=data.get('title')
        c=data.get('completed')
        if t=="":
            messages.info(request, "invalid title")
            return redirect(f'/update/{user.id}')
        user.title=t
        if c=="on":
          user.complete=True
        else:
            user.complete=False
        user.save()
        return redirect('/')
    context={'queryset':user}
    return render(request,'update.html',context)

def delete(request,id):
    user=Task.objects.get(id=id)
    if request.method == "POST":
        user.delete()
        return redirect('/')
    context={'queryset':user}
    return render(request,'delete.html',context)