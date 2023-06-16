from django.shortcuts import render,redirect
from luminar.models import Student

# Create your views here.
def student(req):
    return render(req, 'add_student.html')

def addstudent(req):
    if req.method=='POST':
        na=req.POST.get('name')
        mob=req.POST.get('mob')
        emai=req.POST.get('email')
        pla=req.POST.get('palce')
        cour=req.POST.get('course')
        img = req.FILES['image']
        obj = Student(name=na, mobile=mob, email=emai, place=pla, course=cour, image=img)
        obj.save()
        return redirect(student)

def showstudent(req):
    data=Student.objects.all()
    return render(req, 'display_student.html',{'data':data})
