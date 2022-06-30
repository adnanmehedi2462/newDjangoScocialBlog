from django.contrib import admin

# Register your models here.
from USER.models import *
# Register your models here.
 
class allprofile(admin.ModelAdmin):
    list_display=["__str__",'user','image']
    list_per_page = 10

admin.site.register(Profile,allprofile) 