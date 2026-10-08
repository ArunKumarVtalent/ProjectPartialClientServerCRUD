from django.db import models

# Create your models here.
class Department(models.Model):
    DeptNo = models.AutoField(primary_key=True)
    Dname = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)

    class Meta:
        db_table = 'department'

    def __str__(self):
        return self.Dname

class Employee(models.Model):
    EmpId = models.AutoField(primary_key=True)
    Ename = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10)
    Phone = models.CharField(max_length=15)
    Email = models.CharField(max_length=100)
    DOB = models.DateField()
    Salary = models.DecimalField(max_digits=10, decimal_places=2)
    Address = models.CharField(max_length=200)
    DeptNo = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='DeptNo')

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.Ename