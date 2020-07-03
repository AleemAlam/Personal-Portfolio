from django.db import models

# Create your models here.

class AddServices(models.Model):
    service_title = models.CharField(max_length = 100)
    details = models.TextField(max_length = 500)
    iconclass = models.CharField(max_length = 100,blank=True)

    def __str__(self):
        return self.service_title

class MyProject(models.Model):
    title = models.CharField(max_length= 100)
    website_url= models.URLField()
    img = models.ImageField(upload_to = 'images')
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.title
