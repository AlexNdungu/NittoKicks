from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Product Status Sold Out/Avaiable
class productStatus(models.Model):
  
    STATUS = [
        ('AVAILABLE','Available'),
        ('SOLD OUT','Sold Out'),
    ]

    status = models.CharField(choices=STATUS,max_length=100, primary_key=True, default='AVAILABLE')

    def __str__(self):
        return self.status

#The Shoe Type sex
class productCategory(models.Model):

    CATEGORY = [
        ('NONE','None'),
        ('MALE','Male'),
        ('FEMALE','Female'),
    ]  

    category = models.CharField(choices=CATEGORY ,max_length=100, primary_key=True, default='NONE')      

    def __str__(self):
        return self.category


#Order Part
class receivedOrder(models.Model):

    SEEN = [
        ('VIEWING','Viewing'),
        ('VIEWED','Viewed'),
    ]

    seen = models.CharField(choices=SEEN ,max_length=100, primary_key=True, default='VIEWING')

    def __str__(self):
        return self.seen

#Payment Status
class paymentStatus(models.Model):

    PAYMENT_STATUS =[
        ('UNPAID','Unpaid'),
        ('PAID','Paid'),
    ]

    pay_status = models.CharField(choices=PAYMENT_STATUS, max_length=100, primary_key=True, default='UNPAID')

    def __str__(self):
        return self.pay_status

#Sending Status
class sentStatus(models.Model):

    SENT_STATUS = [
        ('SENDING','Sending'),
        ('SENT','Sent'),
    ]

    sent_status = models.CharField(choices=SENT_STATUS, max_length=100, primary_key=True, default='SENDING')        
        
    def __str__(self):
        return self.sent_status    

#Delivery Status
class deliveryStatus(models.Model):

    DELIVERY_STATUS = [
        ('PENDING','Pending'),
        ('DELIVERED','Delivered'),
    ]

    delivery_status = models.CharField(choices=DELIVERY_STATUS, max_length=100, primary_key=True, default='PENDING') 

    def __str__(self):
        return self.delivery_status      


#Shoes Brand
class Brands(models.Model):
    brand = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.brand

#County Residence
class County(models.Model):
    county = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.county        

#Products Relation
class Products(models.Model):
    shoe_id = models.AutoField(primary_key=True)
    shoe_image = models.ImageField(blank=True, null=True, verbose_name='Shoe Image')
    shoe_brand = models.ForeignKey(Brands, on_delete = models.CASCADE)
    shoe_name = models.CharField(max_length=100, blank=True, null=True)   
    shoe_sex = models.ForeignKey(productCategory, on_delete = models.CASCADE, default='NONE')
    shoe_availability = models.ForeignKey(productStatus, on_delete = models.CASCADE, default='AVAILABLE')
    price = models.FloatField(blank=True, null=True, verbose_name='Price') 
    colors = models.CharField(max_length=100, blank=True, null=True, verbose_name='Colors Available')
    shoe_size_from = models.IntegerField(blank=True, null=True, verbose_name='Shoe-Size-From')
    shoe_size_to = models.IntegerField(blank=True, null=True, verbose_name='Shoe-Size-To')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Date Added')

    def __str__(self):
        return self.shoe_name

    @property
    def image_url(self):
        if self.shoe_image and hasattr(self.shoe_image, 'url'):
            return self.shoe_image.url    

#Customer Profile
class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    sex = models.ForeignKey(productCategory, on_delete = models.CASCADE,default='NONE')
    first_name = models.CharField(max_length=100, blank=True, null=True, default='FirstName')
    last_name = models.CharField(max_length=100, blank=True, null=True, default='LastName')
    profile_pic = models.ImageField(blank=True, null=True, verbose_name='Profile Image')
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=100,default='2547', null=True)
    county = models.ForeignKey(County, on_delete = models.CASCADE, default='Nairobi' )
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='Date Registered')

    @property
    def Profimage_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url    

    def __str__(self):
        return self.user.username       