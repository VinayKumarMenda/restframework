from django.db import models

# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    #image=models.ImageField(upload_to='profiles')
    def __str__(self):
        return self.name