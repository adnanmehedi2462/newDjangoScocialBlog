from django.urls import path
from .import views 
from .urls import *
from .views import *
urlpatterns = [
    path('',Home.as_view(),name="content"),
    path('Newpost',allnewpost.as_view(),name="post"),
    # path('Details/<int:pk>/',views.detailall,name="detail"),
    path('Detail_Post/<int:pk>/',detailall.as_view(),name="detail"),
    # path('writer/<int:pk>/',views.writerall,name="writer"),
    path('writer/<int:pk>/',writerall.as_view(),name="writer"),
    path('deletepost/<int:pk>/',deletepost.as_view(),name="deletepost"),
    
    path('Updatepost/<int:pk>/',Updatepost.as_view(),name="Updatepost"),
  	
    path('profile_view/<name>',views.sameuserposts,name="profile_view"),
]
