from django.db import models
from monan.models import Post
class Cart(models.Model):
    product =  models.ManyToManyField(Post, null= True, blank=True)
    total = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Cart id: %s" %str(self.id)