from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class Watch(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    watch_title = models.CharField(max_length=50)
    watch_pic = models.ImageField(upload_to='watches/')
    watch_detail = models.CharField(max_length=200)
    watch_price = models.CharField(max_length=10)

    def __str__(self):
        return str(self.watch_title)

# create model function to use multiple time 
    # @staticmethod
    # def get_products_by_id(ids):
    #     return Watch.objects.filter(id__in =ids)

    # @staticmethod
    # def get_all_products():
    #     return Watch.objects.all()


class Order(models.Model):
    product = models.ForeignKey(Watch,on_delete=models.CASCADE)
    # customer = models.ForeignKey(Register,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50,default='', blank=True)
    phone = models.CharField(max_length=15,default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)

    def placeOrder(self):
        self.save()