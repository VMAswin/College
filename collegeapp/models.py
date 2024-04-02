from django.db import models
from django.contrib.auth.models import User
class Course(models.Model):
    course_Name=models.CharField(max_length=255)
    Fees=models.IntegerField(null=True)

class Student(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    Student_Name=models.CharField(max_length=255)
    Student_Address=models.CharField(max_length=255)
    Age=models.IntegerField(null=True,blank=True,default=1)
    Joining_Date=models.DateField()

class Teacher(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    Address=models.CharField(max_length=255)
    Age=models.IntegerField(null=True)
    Contact_No=models.CharField(max_length=255)
    Image=models.ImageField(upload_to="image/",null=True)
