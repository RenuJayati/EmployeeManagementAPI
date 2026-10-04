from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    EmployeeViewSet,
    DepartmentViewSet,
    dashboard,
    employee_list,
    add_employee,
    edit_employee,
    delete_employee,
    department_list,
    login_view,
    logout_view,

)

router = DefaultRouter()

router.register('employees', EmployeeViewSet)
router.register('departments', DepartmentViewSet)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('', dashboard, name='dashboard'),
    path('employees/', employee_list, name='employee_list'),
    path('employees/add/', add_employee, name='add_employee'),
    path('employees/edit/<int:id>/', edit_employee, name='edit_employee'),
    path('employees/delete/<int:id>/', delete_employee, name='delete_employee'),
    path('departments/', department_list, name='department_list'),

]

urlpatterns += router.urls