from django.db import models

# Create your models here.


class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)

class postsdata(models.Model):
    post_name = models.CharField(max_length=100)
    post_type = models.CharField(max_length=100)
    post_date = models.DateField()
    post_content=models.TextField()

# class employees(models.Model):
#     ename = models.CharField(max_length=100)
#     age = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     esalary = models.CharField(max_length=100)
 