from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection

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
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employee")
        employees = cursor.fetchall()
        cursor.close()
        return Response({"employees": employees}, status=status.HTTP_200_OK)

class GetEmployeeById(APIView):
    pass

class CreateEmployee(APIView):
    pass

class UpdateEmployee(APIView):
    pass

class DeleteEmployee(APIView):
    pass

class GetAllDepartments(APIView):
    pass