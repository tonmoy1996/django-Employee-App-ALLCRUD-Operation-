from django.shortcuts import render,redirect
from .models import Employee,Position
from .forms import EmployeeForm

# Create your views here.
# pip install django-crispy-forms
def employee_list(request):
    emp=Employee.objects.all()
    context={'emp':emp}
    return render(request,'employee_register/employee_list.html',context)



def employee_form(request,id=0):

    form=EmployeeForm() 

    if request.method == 'POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list')

    context={'form': form}
    return render(request,'employee_register/employee_form.html',context)


def employee_update(request,id):

    emp=Employee.objects.get(pk=id)
    form=EmployeeForm(instance=emp)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
        return redirect('list')
    context={'form': form}
    return render(request,'employee_register/employee_update.html',context)


def employee_delete(request,id):
    emp=Employee.objects.get(pk=id)
    form=EmployeeForm(instance=emp)
    if request.method == 'POST':
        Employee.objects.filter(id=id).delete()
        return redirect('list')

    context={'form':form}
    return render(request,'employee_register/employee_delete.html',context)