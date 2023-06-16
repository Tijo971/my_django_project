from django.shortcuts import render,redirect
from student_app.models import student
# Create your views here.
def student(req):
    return render(req, 'index.html')

def savedata(req):
    if req.method == 'POST':
        nme=req.POST.get('name')
        ag=req.POST.get('age')
        obj=student(name=nme, age= ag)
        obj.save()
        return redirect(student)
