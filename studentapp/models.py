from django.db import models

# Create your models here.
class student(models.Model):
    student_name=models.CharField(max_length=255,null=True)
    address=models.TextField()
    age=models.IntegerField()
    email=models.EmailField()
    joining_date=models.DateField()
    qualification = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    contact_number=models.CharField(max_length=255,null=True)
