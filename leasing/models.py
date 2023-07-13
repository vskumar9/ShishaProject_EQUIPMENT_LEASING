from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models import Sum


#Create User details Store model
class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=30)
    Phone = models.BigIntegerField()
    Gender = models.CharField(max_length=10)
    Address = models.CharField(max_length=50)
    TermAndConditions = models.BooleanField(default=True)
    forget_password_token = models.CharField(max_length=100, default=None)

#Create Containers Details Store model
class Container(models.Model):
    Name = models.CharField(max_length=100)
    Price = models.IntegerField(default=0)
    Image = models.ImageField()
    No_of = models.IntegerField(default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)

    # Once user booked containers to no.of contaiers to remove to store the available containers number
    def available_quantity(self):
        booked_quantity = Booking.objects.filter(container=self).aggregate(total=Sum('No_of'))['total']
        if booked_quantity is None:
            booked_quantity = 0
        return self.No_of - booked_quantity


#Create Booking all users data to store the Booking Model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    userdetail = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(default=datetime.datetime.now())
    No_of = models.IntegerField()
    confirm = models.BooleanField(default=False)
