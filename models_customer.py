from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_lenght=50)


    def __str__(self):
        return self.make + ' ' + self.customermodel