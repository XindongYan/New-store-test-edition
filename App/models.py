from django.db import models


class User(models.Model):
    username = models.CharField(null=True, blank=True, max_length=50)
    password = models.CharField(null=True, blank=True, max_length=1000)

    def __str__(self):
        return self.username

# 为手机模型
class Store(models.Model):
    name = models.CharField(null=True, blank=True, max_length=1000)
    unit = models.IntegerField(null=True, blank=True)
    images = models.FileField(upload_to='media/')

    def __str__(self):
        return self.name


# 为物件模型
class Thing(models.Model):
    name = models.CharField(null=False, blank=False, max_length=1000)
    unit = models.IntegerField(null=False, blank=False)
    images = models.FileField(upload_to='thing')

    def __str__(self):
        return self.name


# 为电脑模型
class Mac(models.Model):
    name = models.CharField(null=False, blank=False, max_length=1000)
    unit = models.IntegerField(null=False, blank=False)
    images = models.FileField(upload_to='pc')

    def __str__(self):
        return self.name
