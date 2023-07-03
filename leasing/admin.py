from django.contrib import admin

# Register your models here.
from .models import UserDetails, Booking, Container

admin.site.register(UserDetails)
admin.site.register(Container)
admin.site.register(Booking)
