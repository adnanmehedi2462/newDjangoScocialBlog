



from multiprocessing import context
from operator import truth
from django.contrib import messages



from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm


from .forms import createform,editform,updateProfile,dflt
from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404,HttpResponse,Http404,redirect,HttpResponseRedirect

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView





from  post.models import *
from USER.models import *



from .models import *
# Create your views here.
# def  register(request):
#     url = request.META.get('HTTP_REFERER')
#     if request.method == "POST":  
#         username=request.POST['username']
#         password=request.POST['password']
#         confirm_password=request.POST['confirm_password']

#         if password == confirm_password:
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, 'User name already exists !!')
#             else:
#                 user=User.objects.create_user(username=username,password=password)
#                 user.is_active=True
#                 user.is_staff=True
#                 user.save()
#                 return redirect ("/")

#         else:
#             messages.error(request, 'Password not match !!')
#             return HttpResponseRedirect(url)
         
            
            

#     return render(request,"register.html")
    

    

def register(request):
    if request.user.is_authenticated:
        return redirect("/") 
    else:
                
        form=createform()
        
        if request.method=='POST': 
            
            form=UserCreationForm(request.POST)
                  
            if form.is_valid():
                form.save()
                return redirect("userlogin")
                                    
            else:
                messages.success(request,'something Wrong !!')

                
        context={
            "form":form
        }
        return render(request,"register.html",context)
        
    
    
    
# class base view

# class editprofile(View):
#     def get(self,request):
#         form=UserCreationForm()
#         context={
#             "form":form
#         }
#         return render(request,"register.html",context)
#     def post(self,request):
#         url = request.META.get('HTTP_REFERER')
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("userlogin")
#         else:
#             messages.success(request,'something Wrong !!')
#             return HttpResponseRedirect(url)
           
               
 
    
    
    
def userlogin (request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":
            username=request.POST.get("username")
            password=request.POST.get("password")
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                messages.success(request,'Username or Password is wrong !!')
                
        
                
        return render(request,"login.html")

def userlogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("userlogin")
    else:
        return redirect("/")
    
    
    
    
    
class profile (View):
    
    def get(self,request):
        
        
        if request.user.is_authenticated:
            
            user = request.user
            user_posts=Post.objects.filter(author=request.user).order_by("-id")
            context={
                "user":user,
                "user_posts":user_posts,
            }
                    
        
            return render(request,"profile.html",context)
        else:
            return redirect("userlogin")


    



            
        
def editprofile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form = editform(request.POST, instance=request.user)
            profile_form = updateProfile(request.POST, request.FILES, instance=request.user.profile)
            if form.is_valid() and profile_form.is_valid():
                form.save() 
                profile_form.save()
                print(profile_form)
                return redirect("profile")
        else:  
            
            form=editform(instance=request.user)
            profile_form=updateProfile(instance=request.user.profile)
        context={
            "form":form,
            "profile_form":profile_form
        }
        return render(request,"editprofile.html",context)
    else:
        return redirect("userlogin")
            
            
        
        
    
        