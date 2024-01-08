from django.shortcuts import render,redirect
from studentapp.models import student



# Create your views here.
def show_student(request):
    return render(request,"student.html")
def add_student(request):
    if request.method=='POST':
        
        ename=request.POST['student_name']
        add=request.POST['student_address']
        age=request.POST['student_age']
        email=request.POST['student_email']
        jodate=request.POST['joining']
        quali=request.POST['student_qualification']
        gender=request.POST['student_gender']
        number=request.POST['contact_num']
        std=student(student_name=ename,address= add,age=age,email=email,joining_date=jodate,qualification=quali,gender=gender,contact_number=number)
        std.save()
    return redirect('show_student_details')
def show_student_details(request):
    Student=student.objects.all()
    return render(request,"show_student_details.html",{'std':Student})  
def editpage(request,pk):
    std=student.objects.get(id=pk)
    return render(request,'editpage.html',{'Student':std})
def edit_student_details(request,pk):
    if request.method=='POST':
        std=student.objects.get(id=pk)
        std.student_name=request.POST.get('std_name')
        std.address=request.POST.get('add')
        std.age=request.POST.get('age')
        std.email=request.POST.get('email')
        std.joining_date=request.POST.get('join')
        std.qualification=request.POST.get('student_qualification')
        std.gender=request.POST.get('student_gender')
        std.contact_number=request.POST.get('contact_num')
        std.save()
        return redirect('show_student_details')
    return render(request,"editpage.html")
def deletepage(request,pk):
    std=student.objects.get(id=pk)
    std.delete()
    return redirect('show_student_details')

def details(request,pk):
    std=student.objects.get(id=pk)

    return render(request,"details.html",{'details':std})
    