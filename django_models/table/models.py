from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class User(models.Model):
    user_id  = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    username = models.CharField(max_length=150, unique=True)
    email    = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Encrypt password before saving
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

class Address(models.Model):
    address_id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    street     = models.CharField(max_length=255)
    city       = models.CharField(max_length=100)
    state      = models.CharField(max_length=100)
    zip_code   = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} - {self.zip_code}"

class PhoneNumber(models.Model):
    phone_id     = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    phone_number = models.CharField(max_length=20)
    phone_type   = models.CharField(max_length=50, choices=[('Mobile', 'Mobile'), ('Home', 'Home'), ('Work', 'Work')])

    def __str__(self):
        return f"{self.phone_number} ({self.phone_type})"

class Profession(models.Model):
    profession_id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    title         = models.CharField(max_length=100)
    description   = models.TextField()

    def __str__(self):
        return self.title

# Model that unites all information related to the User
class UserProfile(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    address      = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, related_name='user_addresses')
    phone_number = models.ForeignKey(PhoneNumber, on_delete=models.SET_NULL, null=True, related_name='user_phone_numbers')
    profession   = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True, related_name='user_professions')

    def __str__(self):
        return f"Profile of {self.user.username}"
