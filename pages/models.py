from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # additional table
    contact = models.BigIntegerField()
    address = models.CharField(max_length=300)
    pincode = models.IntegerField()

    def __str__(self):
        return str(self.user.username)

# Product Order Model
class order_list(models.Model):
    product = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.product)