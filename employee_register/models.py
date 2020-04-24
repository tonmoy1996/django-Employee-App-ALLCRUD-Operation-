from django.db import models

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Employee(models.Model):
    fullname=models.CharField(max_length=100)
    empcode=models.CharField(max_length=10)
    mobile=models.CharField(max_length=20)
    position=models.ForeignKey(Position, on_delete=models.CASCADE)