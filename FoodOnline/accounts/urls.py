from django.urls import path

from . import views

urlpatterns = [
    path('registerUser/',views.registerUser,name='registerUser'),
    path('registerVendor/',views.registerVendor,name='registerVendor'),

    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('my-account/', views.my_account, name='myAccount'),
    path('dashboard/',views.custDashboard,name='custDashboard')

]
