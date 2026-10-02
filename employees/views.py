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