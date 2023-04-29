from django.shortcuts import render,HttpResponse
from geopy.geocoders import Nominatim
# from dukaan.models import Contact


from rest_framework import status

from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from .models import dukan_user,contact_us
from .models import *

# Create your views here.
@api_view(['GET'])
@csrf_exempt
def login_page(request):

    return render(request,'html/login.html')



@api_view(['GET'])
@csrf_exempt
def dashboard(request):

    return render(request,'html/dashboard.html')



@api_view(['GET'])
@csrf_exempt
def contact_us(request):

    return render(request,'html/contact_us.html')



@api_view(['GET'])
@csrf_exempt
def about_us(request):

    return render(request,'html/about_us.html')



@api_view(['GET'])
@csrf_exempt
def services(request):

    return render(request,'html/services.html')



@api_view(['GET'])
@csrf_exempt
def index(request):

    return render(request,'html/index.html')





@api_view(['GET'])
@csrf_exempt
def register(request):

    return render(request,'html/register.html')








@api_view(['POST'])
@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&444')
        try:
            shop_name= request.POST['shop_name']
            mobile_number= request.POST['mob']
            password= request.POST['pass1']
            email= request.POST['email']
            category= request.POST['category']        
            media = request.FILES['media']
            print(media)       
            # calling the Nominatim tool
            try:
                loc = Nominatim(user_agent="GetLoc")
                address= request.POST['address']
                # entering the location name
                getLoc = loc.geocode(f"{address}")
                lat = getLoc.latitude
                lang = getLoc.longitude
            except:
            # printing address
                address= request.POST['address']
                lat ="26.8467"
                lang ="80.9462"
            # printing latitude and longitude
            # print("Latitude = ", getLoc.latitude, "\n")
            # print("Longitude = ", getLoc.longitude)
            
            # print(mobile_number,address,"*********************")
            c_obj = dukan_user.objects.create(shop_name=shop_name,password =password,address=address,mobile_number=mobile_number,email_address = email,lat = lat,lng=lang,category=category,media=media)
            print(c_obj,"&&&&&&&")
            DATA = {'msg': 'created'}
            return render(request,'html/submit.html') 
        except Exception as e:
            print(e)
            return render(request,'html/error.html')
        

@api_view(['GET'])
@csrf_exempt
def get_shop(request):
    if request.method == 'GET':
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&333')
        response = []
        try:
            
            c_obj = dukan_user.objects.all().values()
            print(c_obj,"jjjjj")
            i_obj = shop_category.objects.all().values()
            print(i_obj,"jjjjj********************************8")
           

        

            data = {'data':c_obj,
                    'category':i_obj}
            print(data,"hhhh")
            return render(request,'html/index.html',context=data)
        except:
            return render(request,'html/index.html')
        
        
@api_view(['GET'])
@csrf_exempt
def find_shop(request):
    if request.method == 'GET':
        shop_categories=request.GET['shop_categories']
        shop_name=request.GET['shop_name']
        km = 15
        
        try:
            loc = Nominatim(user_agent="GetLoc")
            address= request.GET['address']
            # entering the location name
            getLoc = loc.geocode(f"{address}")
            lat = getLoc.latitude
            lang = getLoc.longitude
        except:
        # printing address
            address= request.GET['address']
            lat ="26.8467"
            lang ="80.9462"
        
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&222')
        response = []
        try:
            
            # c_obj = dukan_user.objects.filter(Q(shop_name__icontains=shop_name,lat=lat,lng=lang,category=shop_categories)).values()
            c_obj = dukan_user.objects.filter(shop_name__icontains=shop_name,address=address,category=shop_categories).values()
            print(c_obj,"jjjjj")
            # {"shop_name":i.shop_name,
            # "address":i.address,
            # "category":i.category}

            data = {'data':c_obj}
            print(data,"hhhh")
            return render(request,'html/index.html',context=data)
        except:
            return render(request,'html/error.html')
        
        
        
@api_view(['GET'])
@csrf_exempt
def find_shop_by_category(request):
    if request.method == 'GET':
        print("lsllsls")
        shop_categories='Daily Need'
        
        
        
        response = []
        # try:
            
        c_obj = dukan_user.objects.filter(category__icontains=shop_categories).values()
        print(c_obj,"jjjjj")
        # {"shop_name":i.shop_name,
        # "address":i.address,
        # "category":i.category}

        data = {'data':c_obj}
        print(data,"hhhh")
        return render(request,'html/services.html',context=data)
        # except:
        #     return render(request,'html/index.html')
        
        
@api_view(['POST'])
@csrf_exempt
def contact_us1(request):
    if request.method == 'POST':
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&111')
        try:
            name= request.POST['name']
            mobile_number= request.POST['mob']
            email= request.POST['email']
            remark1= request.POST['remark']        
            # media= request.FILE['media']        
            # calling the Nominatim tool
            
            c_obj = remark.objects.create(name=name,mobile_number=mobile_number,email= email,remark=remark1)
            print(c_obj,"&&&&&&&")
            DATA = {'msg': 'created'}
            return render(request,'html/submit.html')
        except:
            return render(request,'html/index.html')
        


@api_view(['GET'])
@csrf_exempt
def user_login(request):
    if request.method == 'GET':
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&111')
        try:
            name= request.GET['name']
            password= request.GET['password']
                   
            # media= request.FILE['media']        
            # calling the Nominatim tool
            
            c_obj = dukan_user.objects.filter(shop_name=name,password=password)
            print(c_obj,"&&&&&&&")
            data = {'msg': 'created'}
            return render(request,'html/index_new.html',context=data)
        except:
            return render(request,'html/submit.html')

    
@api_view(['GET'])
@csrf_exempt
def get_category(request):
    if request.method == 'GET':
      
  
        print("KKKKKKKKKKKKKKKkk")
        try:
            
            c_obj = shop_category.objects.all().values()
            print(c_obj,"jjjjj********************************8")
           

            category = {'category':c_obj}
       
            return render(request,'html/index.html',context=category)
        except:
            return render(request,'html/error.html')
        
        
@api_view(['GET'])
@csrf_exempt
def home(request):

    return render(request,'html/home.html')


@api_view(['GET'])
@csrf_exempt
def find_resturent(request):
    if request.method == 'GET':
        print("lsllsls")
        shop_categories='Resturent'
        
        
        
        response = []
        # try:
            
        c_obj = dukan_user.objects.filter(category__icontains=shop_categories).values()
        print(c_obj,"jjjjj")
        # {"shop_name":i.shop_name,
        # "address":i.address,
        # "category":i.category}

        data = {'data':c_obj}
        print(data,"hhhh")
        return render(request,'html/resturent.html',context=data)
    
    
@api_view(['PATCH'])
@csrf_exempt
def add_reviews(request):
    if request.method == 'PATCH':
        print("lsllsls")
        reviews =request.data['reviews']
        c_id =request.data['c_id']
        
        c_obj = dukan_user.objects.get(c_id=c_id)
        total_reviews = int(c_obj.reviews) + 1
        total_of_reviews= int(c_obj.post) + int(reviews)
        total_post_user = int(c_obj.total_post_users) + 1
        
        final_reviews = total_of_reviews/total_post_user
        
        
        response = []
        # try:
            
        c_obj = dukan_user.objects.filter(c_id).update(reviews = final_reviews,total_of_reviews=total_of_reviews,total_post_user=total_post_user)
        print(c_obj,"jjjjj")
        # {"shop_name":i.shop_name,
        # "address":i.address,
        # "category":i.category}

        data = {'data':c_obj}
        print(data,"hhhh")
        return render(request,'html/resturent.html',context=data)
    
    
@api_view(['DELETE'])
@csrf_exempt
def add_reviews(request):
    if request.method == 'DELETE':
        
        c_id =request.data['c_id']
        
        
        # try:
            
        c_obj = dukan_user.objects.filter(c_id =c_id).delete()  
        # {"shop_name":i.shop_name,
        # "address":i.address,
        # "category":i.category}

        data = {'data':c_obj}
        print(data,"hhhh")
        return render(request,'html/resturent.html',context=data)
        
