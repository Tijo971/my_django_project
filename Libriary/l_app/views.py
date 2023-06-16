from django.shortcuts import render,redirect
from l_app.models import books,users

# Create your views here.
def mybook(req):
    return render(req, 'add_books.html')


def savedata(req):
    if req.method=="POST":
        bnme=req.POST.get('bname')
        anme=req.POST.get('aname')
        price=req.POST.get('price')
        obj=books(b_nme=bnme, a_nme=anme, pri=price)
        obj.save()
        return redirect(mybook)

def myuser(req):
    return render(req, 'add_users.html')

def saveuser(req):
    if req.method=='POST':
        name=req.POST.get('u_name')
        em=req.POST.get('u_email')
        ag=req.POST.get('u_age')
        moble=req.POST.get('number')
        pr=req.POST.get('u_price')
        obj=users(nme=name, eml=em, age=ag, mob=moble, pri=pr)
        obj.save()
        return redirect(myuser)