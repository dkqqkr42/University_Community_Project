from django.db import models

class User(models.Model):
    userID = models.CharField(max_length=50)
    userPassword = models.CharField(max_length=100)
    userName = models.CharField(max_length=10)
    userEmail = models.CharField(max_length=50)
    userGender = models.CharField(max_length=50)

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)