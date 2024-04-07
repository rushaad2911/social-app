from multiprocessing import context
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView,ListView,CreateView
from faker import Faker 
from django.db import models
from post.models import Post
from accounts.models import CustomUser
import random
from django.urls import reverse_lazy


class HomeView(ListView):


    # data = Post.objects.all()
    # shu = random.shuffle(data)


    model=Post
    template_name = "home.html"
    context_object_name = 'post'

    # extra_context = {post:'post'}

    

 
    
def DummyData(request):
    
    fake = Faker()

    for i in range(1):
        
        Post.objects.create(
            
            post_title = fake.name(),
            post_user = request.user
            
        )
        
    return HttpResponseRedirect(reverse_lazy('homeview'))
