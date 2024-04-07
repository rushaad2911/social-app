from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostTest(TestCase):



    def setUp(self):
        
        self.post = Post.objects.create(
            
            post_title = 'test_post'
            
        )
        
        
        
    def test_allpostpage(self):
        
        post = self.client.get(reverse('allpostview'))

        self.assertTemplateUsed(post,'allpost.html')
        self.assertEqual(post.status_code,200)
        
        

    def test_createpost(self):
        
        createpost = self.client.get(reverse('createpostview'))
        
        self.assertEqual(createpost.status_code,200)
        self.assertTemplateUsed(createpost,'CreatePost.html')
        self.assertEqual(self.post.post_title,'test_post')
        