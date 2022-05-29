from django.db import models

class Noteregister(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=16)
    title_page=models.CharField(max_length=30,default="type")
    summary=models.TextField(max_length=3000)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    coverpicture=models.ImageField(upload_to='images/',null=True)


    def __str__(self):
        return self.title_page

    class Meta:
        ordering=['-updated']

# Create your models here.
