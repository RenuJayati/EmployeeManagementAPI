from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from rest_framework import viewsets, filters
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'designation', 'email']
    ordering_fields = ['name', 'salary', 'joining_date']


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

@login_required
def dashboard(request):

    employees = Employee.objects.all()

    total_employees = employees.count()

    total_departments = Department.objects.count()

    average_salary = employees.aggregate(
        Avg('salary')
    )['salary__avg'] or 0
    highest_salary = employees.order_by('-salary').first()

    recent_employees = employees.order_by('-id')[:5]

    context = {
        'total_employees': total_employees,
        'total_departments': total_departments,
        'average_salary': round(average_salary, 2),
        'highest_salary': highest_salary,
        'recent_employees': recent_employees,
    }

    return render(
        request,
        'employees/dashboard.html',
        context
    )

@login_required
def employee_list(request):
    employees = Employee.objects.all().order_by('-id')

    search = request.GET.get('search')

    if search:
        employees = employees.filter(
            name__icontains=search
        )

    return render(
        request,
        'employees/employee_list.html',
        {'employees': employees}
    )

@login_required
def add_employee(request):

    if request.method == 'POST':

        Employee.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            designation=request.POST.get('designation'),
            salary=request.POST.get('salary'),
            joining_date=request.POST.get('joining_date'),
            department_id=request.POST.get('department')
        )

        return redirect('/employees/')

    departments = Department.objects.all()

    return render(
        request,
        'employees/employee_form.html',
        {'departments': departments}
    )

@login_required
def edit_employee(request, id):

    employee = Employee.objects.get(id=id)

    if request.method == 'POST':

        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.phone = request.POST.get('phone')
        employee.designation = request.POST.get('designation')
        employee.salary = request.POST.get('salary')
        employee.joining_date = request.POST.get('joining_date')
        employee.department_id = request.POST.get('department')

        employee.save()

        return redirect('/employees/')

    departments = Department.objects.all()

    return render(
        request,
        'employees/employee_edit.html',
        {
            'employee': employee,
            'departments': departments
        }
    )

@login_required
def delete_employee(request, id):

    employee = Employee.objects.get(id=id)

    if request.method == 'POST':
        employee.delete()
        return redirect('/employees/')

    return render(
        request,
        'employees/employee_delete.html',
        {'employee': employee}
    )

@login_required
def department_list(request):

    departments = Department.objects.all()

    return render(
        request,
        'employees/department_list.html',
        {'departments': departments}
    )

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/')

        return render(
            request,
            'employees/login.html',
            {'error': 'Invalid username or password'}
        )

    return render(
        request,
        'employees/login.html'
    )

def logout_view(request):

    logout(request)

    return redirect('/login/')