from django.shortcuts import render, redirect, get_object_or_404
from .models import Person, Department # รวมไว้บรรทัดเดียวพอครับ

def index(request):
    query = request.GET.get('q')
    if query:
        all_person = Person.objects.filter(name__icontains=query)
    else:
        all_person = Person.objects.all()
        
    return render(request, "index.html", {"all_person": all_person})

def form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        dept_id = request.POST.get('department')
        
        # ป้องกันเครื่องค้างถ้าไม่ได้เลือกแผนก
        dept = None
        if dept_id:
            dept = get_object_or_404(Department, id=dept_id)
            
        Person.objects.create(name=name, age=age, department=dept)
        return redirect('index')
    
    all_dept = Department.objects.all()
    return render(request, "form.html", {"all_dept": all_dept})

def edit(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == "POST":
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        dept_id = request.POST.get('department')
        if dept_id:
            person.department = get_object_or_404(Department, id=dept_id)
        person.save() 
        return redirect('index')
    
    all_dept = Department.objects.all() # ดึงแผนกไปให้หน้าแก้ไขเลือก
    return render(request, 'edit.html', {'person': person, 'all_dept': all_dept})

def delete(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    person.delete()
    return redirect('index')

def about(request):
    return render(request, "about.html")

def department_list(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            Department.objects.create(name=name)
        return redirect('form') 
        
    departments = Department.objects.all() 
    return render(request, "department.html", {"departments": departments})