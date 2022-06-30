from django.urls import path
from .import views 
from .views import *
urlpatterns = [
    # path('register/',register.as_view(),name="register"),
  
    path('register/',views.register, name='register'),
    path('userlogin/',views.userlogin, name='userlogin'),
    path('logout/',views.userlogout, name='logout'),
    
    path('profile/',profile.as_view(),name="profile"),
    path('editprofile/',views.editprofile, name='editprofile'),
    

    
  	
]
