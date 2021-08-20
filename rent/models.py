from django.db import models

class Table(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.TextField(null=True)
    level = models.IntegerField(null=True)
    date =  models.DateTimeField(auto_now=True)
    phone = models.IntegerField(null=True)
    def __str__(self):
        return self.name