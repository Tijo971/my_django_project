from django.shortcuts import render,redirect
from ShopApp.models import Shopdb, Productdb
from  django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def addshop(req):
    return render(req, 'AddShop.html')

def shop(req):
    if req.method=='POST':
        nme=req.POST.get('name')
        own=req.POST.get('owner')
        mob=req.POST.get('mobile')
        loc=req.POST.get('location')
        img=req.FILES['image']
        obj=Shopdb(na=nme, ow_nm=own, mobile=mob, locat=loc, image=img)
        obj.save()
        return redirect(addshop)

def product(req):
    return render(req, 'AddProduct.html')



def prod(req):
    if req.method=='POST':
        p_nme=req.POST.get('p_name')
        quty=req.POST.get('qnty')
        pri=req.POST.get('price')
        img=req.FILES['image']
        obj=Productdb(p_na=p_nme, qty=quty, price=pri, image=img)
        obj.save()
        return redirect(product)


def showshop(req):
    datas=Shopdb.objects.all()
    return render(req, 'show_shop.html', {'datas': datas})

def showproduct(req):
    datas=Productdb.objects.all()
    return render(req, 'show_product.html', {'datas': datas})

def editshop(req, dataid):
    data=Shopdb.objects.get(id=dataid)
    return render(req, 'edit_shop.html', {'data': data})

def editproduct(req, dataid):
    data=Productdb.objects.get(id=dataid)
    return render(req, 'edit_product.html', {'data': data})

def updateshop(req, dataid):
    if req.method=='POST':
        nme = req.POST.get('name')
        own = req.POST.get('owner')
        mob = req.POST.get('mobile')
        loc = req.POST.get('location')
        try:
            img=req.FILES['image']
            fs = FileSystemStorage()
            file= fs.save(img.name, img)
        except MultiValueDictKeyError:
            file=Shopdb.objects.get(id=dataid).image
        Shopdb.objects.filter(id=dataid).update(na=nme, ow_nm=own, mobile=mob, locat=loc, image=file)
        return redirect(showshop)

def updateproduct(req, dataid):
    if req.method=='POST':
        p_nme = req.POST.get('p_name')
        quty = req.POST.get('qnty')
        pri = req.POST.get('price')
        try:
            img=req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name, img)
        except MultiValueDictKeyError:
            file=Productdb.objects.get(id=dataid).image
        Productdb.objects.filter(id=dataid).update(p_na=p_nme, qty=quty, price=pri, image=file)
        return redirect(showproduct)

def deleteproduct(req, dataid):
    data=Productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(showproduct)


def deleteshop(req, dataid):
    data=Shopdb.objects.filter(id=dataid)
    data.delete()
    return redirect(showshop)

