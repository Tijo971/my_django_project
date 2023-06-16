from django.shortcuts import render, redirect
from my_temp.models import Student,Course
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def demo_temp(req):
    return render(req, 'index.html')

def addstudent(req):
    return render(req, 'add_student.html')

def savedata(req):
    if req.method == 'POST':
        na = req.POST.get('name')
        ag = req.POST.get('age')
        mob = req.POST.get('mobile')
        ema = req.POST.get('email')
        cour = req.POST.get('course')
        addr = req.POST.get('address')
        img = req.FILES['image']
        obj = Student(name=na, age=ag, mobile=mob, email=ema, course=cour, address=addr, imge=img)
        obj.save()
        return redirect(addstudent)

def displaystudent(req):
    data = Student.objects.all()
    return render(req, 'display_student.html', {'data':data})


def editstudent(req, dataid):
    data = Student.objects.get(id=dataid)
    return render(req, 'edit_student.html', {'data':data})

def updatestudent(req, dataid):
    if req.method == 'POST':
        na = req.POST.get('name')
        ag = req.POST.get('age')
        mob = req.POST.get('mobile')
        ema = req.POST.get('email')
        cour = req.POST.get('course')
        addr = req.POST.get('address')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Student.objects.get(id=dataid).imge
        Student.objects.filter(id=dataid).update(name=na, age=ag, mobile=mob, email=ema, course=cour, address=addr, imge=file)
        return redirect(displaystudent)

def deletestudent(req, dataid):
    data=Student.objects.filter(id=dataid)
    data.delete()
    return redirect(displaystudent)

def addcourse(req):
    return render(req,'add_course.html')

def savecourse(req):
    if req.method=='POST':
        na=req.POST.get('course')
        fe=req.POST.get('c_fees')
        dur=req.POST.get('duration')
        des=req.POST.get('description')
        insti=req.POST.get('institute')
        img = req.FILES['image']
        obj=Course(course_name=na, fees=fe, duration=dur, description=des, institute=insti, image=img)
        obj.save()
        return redirect(addcourse)


def displaycourse(req):
    data = Course.objects.all()
    return render(req,'display_course.html',{'data':data})

def editcourse(req, dataid):
    data = Course.objects.get(id=dataid)
    return render(req, 'edit_course.html', {'data':data})

def updatecourse(req, dataid):
    if req.method=='POST':
        na = req.POST.get('course')
        fe = req.POST.get('c_fees')
        dur = req.POST.get('duration')
        des = req.POST.get('description')
        insti = req.POST.get('institute')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Course.objects.get(id=dataid).imge
        Course.objects.filter(id=dataid).update(course_name=na, fees=fe, duration=dur, description=des, institute=insti, image=file)
        return redirect(displaycourse)


def deletecourse(req,dataid):
    data=Course.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycourse)

def log(req):
    return render(req,'admin_login.html')

def worklogin(req):
    if req.method=='POST':
        usrnme=req.POST.get('uname')
        pwd=req.POST.get('pswd')
        if User.objects.filter(username__contains=usrnme).exists():
            user = authenticate(username=usrnme, password=pwd)
            if user is not None:
                login(req, user)
                req.session['username']=usrnme
                req.session['password']=pwd
                return redirect(demo_temp)
            else:
                return redirect(log)
        else:
            return redirect(log)

def admin_logout(req):
    del req.session['username']
    del req.session['password']
    return redirect(log)





