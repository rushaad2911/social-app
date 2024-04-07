from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DetailView,DeleteView
from faker import Faker 
from django.db import models
from .models import Post
from accounts.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin


    
class CreatePostView(LoginRequiredMixin,CreateView):
    
    model = Post
    template_name = 'CreatePost.html' 
    fields = ('post_title','gerens','post_image')
    login_url = 'account_login'
    
    def form_valid(self,form):
        form.instance.post_user = self.request.user
        return super().form_valid(form)
        
        
    
    success_url = reverse_lazy('homeview')
    
    
class DetailPostView(DetailView):
    
    model = Post 
    template_name = 'detailpost.html'
    context_object_name = 'post'
 
    
class DeletePostView(DeleteView):
    
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('homeview')
    
