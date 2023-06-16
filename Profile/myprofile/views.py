from django.shortcuts import render, redirect
from myprofile.models import images,datas,Employe

# Create your views here.
def profile(req):
    return render(req, 'index.html')

def imagefn(req):
    if req.method == 'POST':
        nme= req.POST.get('p_name')
        img= req.FILES['image']
        obj= images(name=nme, image=img)
        obj.save()
        return redirect(profile)

def detailsview(req):
    return render(req, 'details.html')

def savedetails(req):
    if req.method == 'POST':
        na=req.POST.get('name')
        adder=req.POST.get('address')
        numb=req.POST.get('num')
        ema=req.POST.get('email')
        cou=req.POST.get('course')
        ima=req.FILES['img']
        obj=datas(n=na, add=adder,mob=numb,em=ema,cour=cou, img=ima)
        obj.save()
        return redirect(detailsview)

def employee(req):
    return render(req, 'employee.html')

def empdata(req):
    if req.method=='POST':
        na=req.POST.get('name')
        mob=req.POST.get('mobile')
        email=req.POST.get('email')
        compa=req.POST.get('company')
        salary=req.POST.get('salary')
        ima=req.FILES['image']
        obj=Employe(nme=na,mobi=mob,ema=email,comp=compa,sal=salary,img=ima)
        obj.save()
        return redirect(employee)
