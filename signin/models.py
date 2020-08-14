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

class Monday(models.Model):
    class1 = models.CharField(max_length=50)
    class2 = models.CharField(max_length=50)
    class3 = models.CharField(max_length=50)
    class4 = models.CharField(max_length=50)
    class5 = models.CharField(max_length=50)
    class6 = models.CharField(max_length=50)
    class7 = models.CharField(max_length=50)
    class8 = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Tuesday(models.Model):
    class1 = models.CharField(max_length=50)
    class2 = models.CharField(max_length=50)
    class3 = models.CharField(max_length=50)
    class4 = models.CharField(max_length=50)
    class5 = models.CharField(max_length=50)
    class6 = models.CharField(max_length=50)
    class7 = models.CharField(max_length=50)
    class8 = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Wednesday(models.Model):
    class1 = models.CharField(max_length=50)
    class2 = models.CharField(max_length=50)
    class3 = models.CharField(max_length=50)
    class4 = models.CharField(max_length=50)
    class5 = models.CharField(max_length=50)
    class6 = models.CharField(max_length=50)
    class7 = models.CharField(max_length=50)
    class8 = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Thursday(models.Model):
    class1 = models.CharField(max_length=50)
    class2 = models.CharField(max_length=50)
    class3 = models.CharField(max_length=50)
    class4 = models.CharField(max_length=50)
    class5 = models.CharField(max_length=50)
    class6 = models.CharField(max_length=50)
    class7 = models.CharField(max_length=50)
    class8 = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Friday(models.Model):
    class1 = models.CharField(max_length=50)
    class2 = models.CharField(max_length=50)
    class3 = models.CharField(max_length=50)
    class4 = models.CharField(max_length=50)
    class5 = models.CharField(max_length=50)
    class6 = models.CharField(max_length=50)
    class7 = models.CharField(max_length=50)
    class8 = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


