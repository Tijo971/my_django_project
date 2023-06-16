from django.shortcuts import render,redirect
from student.models import stud_reg

# Create your views here.
def stud(req):
    return render(req,'student.html')

def reg(req):
    if req.method=='POST':
        nme=req.POST.get('s_name')
        eml=req.POST.get('s_email')
        mob=req.POST.get('s_mob')
        add=req.POST.get('address')
        obj=stud_reg(name=nme, email=eml, mobile=mob, address=add)
        obj.save()
        return redirect(stud)
