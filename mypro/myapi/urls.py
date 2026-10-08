from django.urls import path
from .views import HelloView, GetAllEmployee, GetEmployeeById, CreateEmployee, UpdateEmployee, DeleteEmployee, GetAllDepartments

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('hello/<str:name>/', HelloView.as_view(), name='hello-with-id'),
    path('get-all-employees/', GetAllEmployee.as_view(), name='get-all-employees'),
    path('get-employee-by-id/<int:empid>/', GetEmployeeById.as_view(), name='get-employee-by-id'),
    path('create-employee/', CreateEmployee.as_view(), name='create-employee'),
    path('update-employee/<int:empid>/', UpdateEmployee.as_view(), name='update-employee'),
    path('delete-employee/<int:empid>/', DeleteEmployee.as_view(), name='delete-employee'),
    path('get-all-departments/', GetAllDepartments.as_view(), name='get-all-departments'),
]