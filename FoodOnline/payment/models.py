# from django.db import models

# # Create your models here.
# # orders app, models.py
# # one pending task is save() method call on vendor form
# # pending model creation for the FoodItem


# import json
# from django.db import models
# from accounts.models import User
# from menu.models import FoodItem
# from vendor.models import Vendor


# class Payment(models.Model):
#     PAYMENT_METHOD = (
#         ('PayPal', 'PayPal'),
#         ('RazorPay', 'RazorPay'), # Only for Indian clients    
# )
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     transaction_id = models.CharField(max_length=100)
#     payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=100)
#     amount = models.CharField(max_length=10)
#     status = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def _str_(self):
#         return self.transaction_id


# class Order(models.Model):
#     STATUS = (
#         ('New', 'New'),
#         ('Accepted', 'Accepted'),
#         ('Completed', 'Completed'),
#         ('Cancelled', 'Cancelled'),
#     )

#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
#     vendors = models.ManyToManyField(Vendor, blank=True)
#     order_number = models.CharField(max_length=20)
#     total = models.FloatField()
#     tax_data = models.JSONField(blank=True, help_text = "Data format: {'tax_type':{'tax_percentage':'tax_amount'}}", null=True)
#     total_data = models.JSONField(blank=True, null=True)
#     total_tax = models.FloatField()
#     status = models.CharField(max_length=15, choices=STATUS, default='New')
#     is_ordered = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     # Concatenate first name and last name
#     @property
#     def name(self):
#         return f'{self.first_name} {self.last_name}'


# class OrderedFood(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     fooditem = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     price = models.FloatField()
#     amount = models.FloatField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def _str_(self):
#         return self.fooditem.food_title