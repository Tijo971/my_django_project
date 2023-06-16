from django.shortcuts import render,redirect
from  myshop.models import categorys,product
from webapp.models import UserDB,ContactDB

# Create your views here.

def home(req):
    data=categorys.objects.all()
    return render(req, 'home.html', {'data':data})

def about(req):
    return render(req, 'about.html')

def contact(req):
    return render(req, 'contact.html')

def products(req, cat_nme):
    data=categorys.objects.filter(c_name=cat_nme)
    prod=product.objects.filter(category= cat_nme)
    return render(req, 'products.html',{'data':data, 'prod':prod})

def singlepdt(req, dataid):
    data = product.objects.get(id=dataid)
    pro = product.objects.all()
    return render(req, 'single_pdt.html',{'data':data, 'pro':pro})


def userlogin(arg):
    return render(arg, 'usr_login.html')

def usersignin(arg):
    return render(arg, 'signin_user.html')

def saveuser(req):
    if req.method == 'POST':
        na = req.POST.get('name')
        ema = req.POST.get('email')
        mobi = req.POST.get('mob')
        imag = req.FILES['pfl_img']
        pwd = req.POST.get('pass')
        obj = UserDB(name=na, email=ema, mob_num=mobi, img=imag, passwd=pwd)
        obj.save()
        return redirect(usersignin)


def userloginprocess(req):
    if req.method == 'POST':
        unme = req.POST.get('usrname')
        pwd = req.POST.get('pass')
        if UserDB.objects.filter(name=unme, passwd=pwd).exists():
            req.session['name']=unme
            req.session['passwd']=pwd
            return redirect(home)
        else:
            return redirect(userlogin)
    else:
        return redirect(userlogin)

def userlogout(req):
    del req.session['name']
    del req.session['passwd']
    return redirect(home)


def savecontacts(req):
    if req.method == 'POST':
        na = req.POST.get('name')
        em = req.POST.get('email')
        pn = req.POST.get('phone')
        ms = req.POST.get('msg')
        obj = ContactDB(name=na, email=em, phn_no=pn, msg=ms)
        obj.save()
        return redirect(contact)