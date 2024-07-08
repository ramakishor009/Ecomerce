from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm

# Create your views here.
def index(request):
    itemlist=Item.objects.all()
    #template = loader.get_template('food/index.html')
    context={
        "itemlist":itemlist,
    }
    return render(request,'food/index.html',context)

def item(request):
    return HttpResponse("<h1>this is item page...</h1>")

def details(request,itemid):
    item01 = Item.objects.get(pk=itemid)
    context={ 
        'item01':item01,
    }
    return render(request,'food/details.html',context)
def create_item(request):
    form= ItemForm(request.POST or None)     
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form}) 

def update_item(request,id):
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form,'item':item})

def Delete_item(request,id):
    item=Item.objects.get(id=id)

    if request.method =='POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/item-delete.html',{'item':item})



