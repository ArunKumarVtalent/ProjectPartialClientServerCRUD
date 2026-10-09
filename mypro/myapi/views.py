from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from .models import Employee, Department
from .serialization import EmployeeSerializer, DepartmentSerializer

# Create your views here.
class HelloView(APIView):
    def get(self, request):
        data = {
            "message": "Hello, World! (GET)"
        }
        return Response(data, status=status.HTTP_200_OK)

    def get(self, request):
        name = request.query_params.get('name', 'World')
        data = {
            "message": f"Hello, {name}! (GET)"
        }
        return Response(data, status=status.HTTP_200_OK)

    def get(self, request, name=None):
        data = {
            "message": f"Hello, {name}! (GET)"
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get('name', 'World')
        data = {
            "message": f"Hello, {name}! (POST)"
        }
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request):
        name = request.data.get('name', 'World')
        gender = request.data.get('gender', 'unknown')
        if gender.lower() == 'male':
            data = {
                "message": f"Hello, Mr. {name}! (PUT)"
            }
        elif gender.lower() == 'female':
            data = {
                "message": f"Hello, Ms. {name}! (PUT)"
            }
        else:
            data = {
                "message": f"Hello, {name}! (PUT)"
            }
        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request):
        data = {
            "message": "Hello, World! (DELETE)"
        }
        return Response(data, status=status.HTTP_200_OK)

class GetAllEmployee(APIView):
    def get(self, request):
       empList = Employee.objects.all()
       if empList.exists():
           serializer = EmployeeSerializer(empList, many=True)
           return Response(serializer.data, status=status.HTTP_200_OK)
       return Response("There are no employees available.", status=status.HTTP_404_NOT_FOUND)

class GetEmployeeById(APIView):
    def get(self, request, empid):
        try:
            emp = Employee.objects.get(EmpId=empid)
            if not emp:
                return Response("Employee not found.", status=status.HTTP_404_NOT_FOUND)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response("Employee not found.", status=status.HTTP_404_NOT_FOUND)

class CreateEmployee(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(f"Record created successfully.\n{serializer.data}", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateEmployee(APIView):
    def put(self, request, empid):
        try:
            emp = Employee.objects.get(EmpId=empid)
            serializer = EmployeeSerializer(emp, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(f"Record updated successfully.\n{serializer.data}", status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response("Employee not found.", status=status.HTTP_404_NOT_FOUND)

class DeleteEmployee(APIView):
    def delete(self, request, empid):
        try:
            emp = Employee.objects.get(EmpId=empid)
            if not emp:
                return Response("Employee not found.", status=status.HTTP_404_NOT_FOUND)
            emp.delete()
            return Response(f"Record deleted successfully.", status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response("Employee not found.", status=status.HTTP_404_NOT_FOUND)

class GetAllDepartments(APIView):
    def get(self, request):
        deptList = Department.objects.all()
        if deptList.exists():
            serializer = DepartmentSerializer(deptList, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

class GetEmployeeByEmailPassword(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        password = request.query_params.get('password')
        try:
            emp = Employee.objects.filter(Email=email, Password=password).first()
            if not emp:
                return Response("Employee not found.", status=status.HTTP_404_NOT_FOUND)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response("Employee not found.", status=status.HTTP_404_NOT_FOUND)