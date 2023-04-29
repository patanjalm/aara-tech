from django.db import models

# Create your models here.

# from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import gettext_lazy as _


# class CustomUserManager(BaseUserManager):
#     """
#     Custom user model manager where email is the unique identifiers
#     for authentication instead of usernames.
#     """
#     def create_user(self, email, password, **extra_fields):
#         """
#         Create and save a user with the given email and password.
#         """
#         if not email:
#             raise ValueError(_("The Email must be set"))
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         """
#         Create and save a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("is_active", True)

#         if extra_fields.get("is_staff") is not True:
#             raise ValueError(_("Superuser must have is_staff=True."))
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError(_("Superuser must have is_superuser=True."))
#         return self.create_user(email, password, **extra_fields)
    

# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils.translation import gettext_lazy as _



# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(_("email address"), unique=True)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email
    

class dukan_user(models.Model):
    contact_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=250, blank=True, null=True ,unique=True,)
    address = models.CharField(max_length=1000, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    add_date_time = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    pancard_number = models.CharField(max_length=15, blank=True, null=True)
    adhaar_number = models.CharField(max_length=12, blank=True, null=True)
    mobile_number = models.CharField(unique=True, max_length=13, blank=True, null=True)
    email_address = models.CharField(max_length=150, blank=True, null=True)
    is_mobile_verify = models.IntegerField(default=0,blank=True, null=True)
    is_email_verify = models.IntegerField(default=0,blank=True, null=True)
    gst_number = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(blank=True, null=True,max_length=100)
    lat = models.CharField(max_length=20, blank=True, null=True)
    lng = models.CharField(max_length=20)
    km = models.FloatField(blank=True, null=True)
    media = models.ImageField(upload_to='media',blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    reviews = models.IntegerField(default=0,blank=True, null=True)
 

class reviews(models.Model):
    r_id = models.CharField(primary_key=True, max_length=40)
    contact_id = models.CharField( max_length=40)
    review = models.TextField(blank=True, null=True)
    add_date_time = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    ratting = models.IntegerField(default=5,blank=True, null=True)
    
    
    
class contact_us(models.Model):
    c_id = models.AutoField(primary_key=True)
    remark = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    mobile_number = models.ImageField(blank=True, null=True)
    add_date_time = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
    
class remark(models.Model):
    c_id = models.AutoField(primary_key=True)
    remark = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    mobile_number = models.ImageField(blank=True, null=True)
    add_date_time = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
    
class shop_category(models.Model):
    s_id = models.AutoField(primary_key=True)
    category = models.TextField(blank=True, null=True)
    add_date_time = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    media = models.ImageField(upload_to='media',blank=True, null=True)


    
