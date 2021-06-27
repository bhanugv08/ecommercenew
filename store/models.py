from django.db import models
from django.contrib.auth.models import User,auth


# Create your models here.
class Register(models.Model):
    first_name=models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username



class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, blank=False)
    image = models.ImageField(null=True, blank=True)

    # image

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.ForeignKey(Customer,on_delete=models.CASCADE, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, )
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.customer_name)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total



class OrderItem(models.Model):
    product_name = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,blank=True)
    quantity = models.IntegerField(default=0,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total




class shippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,blank=True,null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.address


