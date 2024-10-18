from django.contrib import admin

# Register your models here.

from . import User, Address, PhoneNumber, Profession, UserProfile

#Apps
admin.site.register(User)
admin.site.register(Address)
admin.site.register(PhoneNumber)
admin.site.register(Profession)
admin.site.register(UserProfile)