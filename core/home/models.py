from django.db import models

class Student(models.Model):
    # id = models.AutoField() -> This is automatocally added by Django and it is a primary key
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    # image = models.ImageField()
    file = models.FileField()

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed =models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name


