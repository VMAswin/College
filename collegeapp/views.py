from django.shortcuts import render,redirect
from collegeapp.models import Course,Student,Teacher
from django.contrib.auth.models import User,auth
from django.contrib.auth import login
from django.contrib import messages
def ho(request):
    return render(request,'home.html')
def test(request):
    return render(request,'test.html')
def teacher(request):
    return render(request,'teacher.html')
def hlog(request):
    if request.method=='POST':
        lname=request.POST['lna']
        lpss=request.POST['lpas']
        lo=auth.authenticate(username=lname,password=lpss)
        if lo is not None:
            if lo.is_staff:
                login(request,lo)
                return redirect('ad')
            else:
                login(request,lo)
                auth.login(request,lo)
                return redirect('teacher')
def ad(request):
    return render(request,'admin.html')
def adco(request):
    return render(request,'add_course.html')
def addcourse(request):
    if request.method=='POST':
        coname=request.POST['cna']
        cofees=request.POST['cfe']
        cou=Course(course_Name=coname,Fees=cofees)
        cou.save()
        return redirect('/')
def adst(request):
    cor=Course.objects.all()
    return render(request,'add_student.html',{'co':cor})
def addstud(request):
    if request.method=='POST':
        stname=request.POST['stna']
        staddre=request.POST['stad']
        stage=request.POST['stag']
        stdate=request.POST['stda']
        stopt=request.POST['se']
        cour=Course.objects.get(id=stopt)
        stud=Student(Student_Name=stname,Student_Address=staddre,Age=stage, Joining_Date=stdate,course=cour)
        stud.save()
        return redirect('ad')
def showstud(request):
    shst=Student.objects.all()
    return render(request,'show_student.html',{'sh':shst})
def shte(request):
    shte=Teacher.objects.all()
    utes=User.objects.all()
    return render(request,'show_teacher.html',{'sht':shte,'ust':utes})
def teacherregist(request):
    cou=Course.objects.all()
    return render(request,'teacher_regist.html',{'cor':cou})
def add_teacher(request):
    if request.method=='POST':
        tfname=request.POST['tfna']
        tlname=request.POST['tlna']
        tuname=request.POST['tuna']
        tpassword=request.POST['tpass']
        tcpassword=request.POST['tcpass']
        taddress=request.POST['tadd']
        tage=request.POST['tage']
        tcontact=request.POST['tcon']
        tmail=request.POST['tema']
        timage=request.FILES['timg']
        topt=request.POST['sel']
        cours=Course.objects.get(id=topt)
        if tpassword==tcpassword:
            if User.objects.filter(username=tuname).exists():
                messages.info(request,'This user name already exists....')
                return redirect('ho')
            else:
                us=User.objects.create_user(
                    first_name=tfname,
                    last_name=tlname,
                    username=tuname,
                    email=tmail,
                    password=tpassword
                )
                us.save()
        else:
            messages.info(request,'Password does not match...')
            return redirect('teacherregist')
        teac=Teacher(Address=taddress,Age=tage,Contact_No=tcontact,Image=timage,course=cours,user=us)
        teac.save()
        return redirect('ho')
def profile(request):
    cur_user=request.user.id
    user1=Teacher.objects.get(user_id=cur_user)
    return render(request,'tprofile.html',{'users':user1})

def ed(request):
    tte=Teacher.objects.get(user=request.user)
    cte=Course.objects.all()
    return render(request,'edit_teacher.html',{'tt':tte,'ct':cte})
def edi(request,k):
    if request.method=='POST':
        teach=Teacher.objects.get(user=k)
        utea=User.objects.get(id=k)
        utea.first_name=request.POST['tfna']
        utea.last_name=request.POST['tlna']
        utea.username=request.POST['tuna']
        teach.Address=request.POST['tadd']
        teach.Age=request.POST['tage']
        teach.Contact_No=request.POST['tcon']
        utea.email=request.POST['tema']
        tcou=request.POST['sel']
        cour=Course.objects.get(id=tcou)
        teach.course=cour
        if 'timg' in request.FILES:
            teach.Image = request.FILES['timg']
        teach.save()
        utea.save()
        return redirect('profile')
    
def logout(request):
    auth.logout(request)
    return redirect('ho')
def delete(request,k):
    tea=Teacher.objects.get(user=k)
    use=User.objects.get(id=k)
    tea.delete()
    use.delete()
    return redirect('shte')
def deletestud(request,k):
    st=Student.objects.get(id=k)
    st.delete()
    return redirect('showstud')
def edits(request,k):
    est=Student.objects.get(id=k)
    eco=Course.objects.all()
    return render(request,'edit_student.html',{'es':est,'ec':eco})
def editstud(request,k):
    if request.method=='POST':
        stude=Student.objects.get(id=k)
        stude.Student_Name=request.POST['stna']
        stude.Student_Address=request.POST['stad']
        stude.Age=request.POST['stag']
        stude.Joining_Date=request.POST['stda']
        sco=request.POST['se']
        cour=Course.objects.get(id=sco)
        stude.course=cour
        stude.save()
        return redirect('showstud')