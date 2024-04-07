from audioop import reverse
from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):
    
    
 
    
    def test_homepage(self):
        
        homepage = self.client.get(reverse('homeview'))
        
        self.assertEqual(homepage.status_code,200)
        self.assertTemplateUsed(homepage,'home.html')
        
        
        
