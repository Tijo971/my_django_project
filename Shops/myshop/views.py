from django.shortcuts import render, redirect
from myshop.models import categorys,product
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from webapp.models import ContactDB

# Create your views here.
def index(req):
    return render(req, 'index.html')

def category(req):
    return render(req, 'add_category.html')

def save_category(req):
    if req.method == 'POST':
        c_nme = req.POST.get('name')
        img = req.FILES['c_image']
        des = req.POST.get('description')
        obj = categorys(c_name=c_nme, c_img=img, c_description=des)
        obj.save()
        return redirect(category)

def disp_category(req):
    data = categorys.objects.all()
    return render(req, 'display_category.html', {'data':data})


def edit_category(req, dataid):
    data = categorys.objects.get(id=dataid)
    return render(req,'edit_category.html', {'data':data})


def updatae_category(req, dataid):
    if req.method=='POST':
        c_nme = req.POST.get('name')
        des = req.POST.get('description')
        try:
            img = req.FILES['c_image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = categorys.objects.get(id=dataid).c_img
        categorys.objects.filter(id=dataid).update(c_name=c_nme, c_img=file, c_description=des)
        return redirect(disp_category)

def delete_category(req, dataid):
    data = categorys.objects.filter(id=dataid)
    data.delete()
    return redirect(disp_category)


def addproduct(req):
    data = categorys.objects.all()
    return render(req, 'add_product.html', {'data':data})

def saveproduct(req):
    if req.method=='POST':
        cate=req.POST.get('category')
        pro_nme=req.POST.get('p_name')
        pri = req.POST.get('price')
        descri=req.POST.get('des')
        bra= req.POST.get('brand')
        img = req.FILES['image']
        obj=product(category=cate, p_name=pro_nme, price=pri, description=descri, brand=bra, image=img)
        obj.save()
        return redirect(addproduct)

def display_product(req):
    data = product.objects.all
    return render(req, 'display_product.html', {'data':data})

def edit_product(req, dataid):
    category = categorys.objects.all()
    products =product.objects.get(id=dataid)
    return render(req, 'edit_product.html', {'category':category, 'products': products})


def update_product(req, dataid):
    if req.method == 'POST':
        cate = req.POST.get('category')
        pro_nme = req.POST.get('p_name')
        pri = req.POST.get('price')
        descri = req.POST.get('des')
        bra = req.POST.get('brand')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = product.objects.get(id=dataid).image
        product.objects.filter(id=dataid).update(category=cate, p_name=pro_nme, price=pri, description=descri, brand=bra, image=file)
        return redirect(display_product)


def delete_product(req, dataid):
    data = product.objects.filter(id=dataid)
    data.delete()
    return redirect(display_product)

def loginpage(req):
    return render(req, 'login_page.html')


def loginprocess(req):
    if req.method=='POST':
        usr_nme=req.POST.get('usrnme')
        pwd = req.POST.get('password')
        if User.objects.filter(username__contains=usr_nme).exists():
            user=authenticate(username=usr_nme, password=pwd)
            if user is not None:
                login(req, user)
                req.session['username']=usr_nme
                req.session['password']=pwd
                return redirect(index)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)


def logout(req):
    del req.session['username']
    del req.session['password']
    return redirect(loginpage)

def displaycontacts(req):
    data = ContactDB.objects.all()
    return render(req, 'contact_info.html', {'data':data})

def deletecontact(req, dataid):
    data = ContactDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycontacts)


