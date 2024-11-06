from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class Category(models.Model):
    category = models.CharField(max_length=50)

class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    gender=models.CharField(max_length=20)
    email=models.CharField(max_length=100)
    registerationdate=models.CharField(max_length=100)
    phonenumber=models.BigIntegerField()
    image=models.CharField(max_length=400)


class Book(models.Model):
    CATEGORY = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publish_year = models.DateField()
    language = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    adddate = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    image = models.CharField(max_length=400)
    description = models.CharField(max_length=1000)


class Order(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    date = models.DateField()
    place = models.CharField(max_length=20)
    pin = models.CharField(max_length=20)
    landmark = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    status = models.CharField(max_length=20)


class Bill_details(models.Model):
    ORDER = models.ForeignKey(Order, on_delete=models.CASCADE)
    BOOK = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status=models.CharField(max_length=100,default="pending")
    reason=models.CharField(max_length=500,default="pending")

class Bill(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()
    status = models.CharField(max_length=20)
    Type = models.CharField(max_length=100)

class Review(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    BOOK = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    rating = models.CharField(max_length=20)
    ORDER = models.ForeignKey(Bill_details,on_delete=models.CASCADE)

class Feedback(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    BOOK = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    feedback = models.CharField(max_length=20)
    ORDER = models.ForeignKey(Bill_details,on_delete=models.CASCADE)

class Complaints(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    complaints=models.CharField(max_length=400)
    date=models.DateField()
    reply=models.CharField(max_length=400)

class Payment(models.Model):
    ORDER = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=200)
    status = models.CharField(max_length=20)

class OfflinePurchaser(models.Model):
    BOOK = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    number = models.BigIntegerField()
    qty = models.IntegerField()
    date = models.DateField()
    place = models.TextField()

