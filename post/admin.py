from django.contrib import admin
from post.models import *
# Register your models here.
 
class allpost(admin.ModelAdmin):
    list_display=["__str__",'author', 'content','image']
    search_fields=['Welcome_text',]
    list_per_page = 10

admin.site.register(Post,allpost) 
