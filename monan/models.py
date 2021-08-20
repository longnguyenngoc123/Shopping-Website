from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=False, blank=True)
    image = models.ImageField(null=True,upload_to='../media/')
    price = models.IntegerField(null=True)
    def __str__(self):
        return self.title
    