from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_lenght=50)
    branch = models.CharField(max_lenght=50)


    def __str__(self):
        return self.make + ' ' + self.employeemodel