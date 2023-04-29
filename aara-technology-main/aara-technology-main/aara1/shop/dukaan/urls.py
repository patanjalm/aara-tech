from django.urls import path
from . views import *
from dukaan import views

urlpatterns = [
    path('',views.get_shop ),
    path('get_shop',views.get_shop ),
    # path('', index),
    path('about_us',views.about_us ,name= 'about_us'),
    path('contact_us',views.contact_us ,name= 'contact_us'),
    path('contact_us1',views.contact_us1 ,name= 'contact_us1'),
    path('services',views.services ,name= 'services'),
    path('index',views.index ,name= 'index'),
    path('login',views.login_page ,name= 'login_page'),
    path('register',views.register ,name= 'register'),
    path('register_user',views.register_user ,name= 'register_user'),
    path('find_shop',views.find_shop ,name= 'find_shop'),
    path('find_shop_by_category',views.find_shop_by_category ,name= 'find_shop_by_category'),
    path('user_login',views.user_login ,name= 'user_login'),
    path('home',views.home ,name= 'home'),
    path('find_resturent',views.find_resturent ,name= 'find_resturent'),
   
   

]