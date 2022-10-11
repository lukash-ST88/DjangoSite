from django.db import models

# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField (auto_now_add=True) # constant date
    time_update = models.DateTimeField(auto_now=True) # changing date
    is_published = models.BooleanField(default=True)


    def __str__(self): # returns data of instances for users
        return self.title

