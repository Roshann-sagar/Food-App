from django.contrib import admin

# Register your models here.
from .models import Category,FoodItem


admin.site.register(Category)
admin.site.register(FoodItem)