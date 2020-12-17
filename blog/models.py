from django.db import models

from django.contrib.auth.models import User
from django.utils.timezone import now

class Blog_Category(models.Model):
    blog_category = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.blog_category

class Blog_Data(models.Model):
    blog_category = models.ForeignKey(Blog_Category,on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=50)
    blog_images = models.ImageField(upload_to='blog/')
    blog_content = models.CharField(max_length=500)
    blog_date = models.DateField()

    def __str__(self):
        return str(self.blog_title)

class BlogComments(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.comment