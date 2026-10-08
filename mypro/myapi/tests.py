from django.test import SimpleTestCase
from .models import Department
from .serialization import DepartmentSerializer


class DepartmentSerializerTests(SimpleTestCase):
    def test_serializes_all_department_fields(self):
        department = Department(DeptNo=1, Dname='Engineering', Location='London')

        serializer = DepartmentSerializer(department)

        self.assertEqual(
            serializer.data,
            {'DeptNo': 1, 'Dname': 'Engineering', 'Location': 'London'},
        )
