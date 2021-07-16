from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(productStatus)
admin.site.register(productCategory)
admin.site.register(receivedOrder)
admin.site.register(paymentStatus)
admin.site.register(sentStatus)
admin.site.register(deliveryStatus)
admin.site.register(Brands)
admin.site.register(Products)
admin.site.register(County)
admin.site.register(Profile)