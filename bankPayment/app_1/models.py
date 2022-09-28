from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model"""
    
    def create_user(self, email, name, password=None):
        """create a new user profile object"""
        
        if not email:
            raise ValueError("Please provide an email address")
        
        email = self.normalize_email(email)
        
        user = self.model(email=email, name=name)
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, password):
        """create and saves a new superuser with given details"""
        
        user = self.create_user(email, name, password)
        
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
            

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent a "User Profile" inside our system."""
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        """Used to get a users fullname."""
        
        return self.name
    
    def get_short_name(self):
        """Used to get a users shortname."""
        
        return self.name
    
    def __str__(self):
        """Django uses this when it needs to convert the object to a string."""
        
        return self.email
    

BANK_CHOICES = (
    ('sonali', 'Sonali'),
    ('rupali', 'Rupali'),
    ('agrani', 'Agrani'),
    ('janata', 'Janata'),
    ('brac', 'BRAC'),
    ('ific', 'IFIC'),
    ('one', 'One'),
    ('dutch', 'Dutch'),
)

class Balance(models.Model):
    userName = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="payment_by")
    taka = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=6, choices=BANK_CHOICES, default='sonali')
    
    def __str__(self):
        return self.taka