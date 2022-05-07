from cgitb import html
from django.shortcuts import redirect, render
from .models import Employee
from .forms import EmployeeForm


# Create your views here.


def employe_home(request):
    employee = Employee.objects.all()
    return render(request, "employee-home.html", {'employee': employee})


def create(request):
    employee = EmployeeForm()
    if request.method == 'POST':
        employee = EmployeeForm(request.POST)
        if employee.is_valid():
            employee.save()
            return redirect('employee-home')
    return render(request, "employee-form.html", {'employee': employee})

def update(request, id):  # to keep both the form html and the edit or update form to work use same variable throught the update def
    employee = Employee.objects.get(id=id)
    employee = EmployeeForm(request.POST or None, instance=employee)
    if employee.is_valid():
        employee.save()
        return redirect('employee-home')

    return render(request, "employee-form.html", {'employee': employee})


def delete(request,id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        employee.delete()
    
        return redirect('employee-home')

    return render(request, "confirm.html",{'employe':employee})

    

