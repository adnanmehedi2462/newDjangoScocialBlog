from multiprocessing import context
from statistics import mode
from urllib import request
from django.shortcuts import render,get_object_or_404,HttpResponse,Http404,redirect,HttpResponseRedirect
from  post.models import *
from USER.models import *
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.views.generic.dates import ArchiveIndexView
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .urls import *
from .forms import editpostform
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
class Home(ArchiveIndexView):
    model=Post
    template_name='content.html'
    paginate_by = 3
    context_object_name='singlepost'
    date_field = "created_at"
    paginate_by = 3
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['slic'] = Post.objects.all().order_by('-id')[:3]
        return context 
        
class detailall(DetailView):
    model=Post
    template_name="details.html"
    context_object_name="singleView"
    
class writerall(DetailView):
    model=Post
    template_name="writer.html"
    context_object_name="writerview"

# def writerall(request,pk):
#     writerview=get_object_or_404(Post,pk=pk)
 
#     context={
#         "writerview":writerview,
   
#     }
#     return render (request,"writer.html",context)


def sameuserposts (request,name):

    all_post=Post.objects.filter(author=name)
    return render(request,"samepost.html",{"all_post":all_post,})
    

# def sameuserposts(request,username):
#     user=request.user
#     sameposts=Post.objects.filter(user=username)
#     # u = User.objects.get(pk=user)
#     context={
       
#         "sameposts":sameposts
#     }
#     return render(request, 'samepost.html', {context})
    
    


    
               


# def detailall(request,pk):
#     singleView=get_object_or_404(Post,pk=pk)
#     context={
#         "singleView":singleView
#     }
#     return render(request,"details.html",context)
    
    
    
    
# def writerall(request,pk):
#     writerview=get_object_or_404(Post,pk=pk)
#     context={
#         "writerview":writerview
#     }
#     return render(request,"writer.html",context)
        

            
# Post new//////////////////////////////////////////////////////////////////////////


class allnewpost (LoginRequiredMixin,CreateView):
    model=Post
    template_name="newpost.html"
    context_object_name="all"
    fields=['title','content','image']
    success_url="/"
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    
    
    
class deletepost(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    template_name="deleteview.html"
    success_url="/"
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
        
class Updatepost(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content','image']
    success_url ="profile"
    template_name="editpost.html"
    # security check ---- same code u can use everywhare
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
            
        return False
    success_url="/"
    
        
    