from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def receipe(request):
    if request.method == "POST":
        data = request.POST

        receipe_img = request.FILES.get('receipe_img')
        receipe_name = data.get('receipe_name')
        receipe_desc = data.get('receipe_desc')

        Recipie.objects.create(
            receipe_img = receipe_img,
            receipe_name = receipe_name,
            receipe_desc = receipe_desc,
        )
        return redirect('/receipe/')
    
    queryset = Recipie.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
     
    context = {'receipes':queryset}
    return render(request,'receipes.html',context)


def delete_receipe(request,id):
    queryset = Recipie.objects.get(id = id)
    queryset.delete()
    return redirect('/receipe/')


def update_receipe(request,id):
    queryset = Recipie.objects.get(id = id)

    if request.method =="POST":
        data = request.POST

        receipe_img = request.FILES.get('receipe_img')
        receipe_name = data.get('receipe_name')
        receipe_desc = data.get('receipe_desc')

        queryset.receipe_name = receipe_name
        queryset.receipe_desc = receipe_desc

        if receipe_img:
            queryset.receipe_img = receipe_img
        
        queryset.save()
        return redirect('/receipe/')
    context = {'receipe' : queryset}
    return render(request,'update_receipes.html',context)