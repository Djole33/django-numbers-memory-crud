from django.db import models
from django.urls import reverse

# Create your models here.

class Guess(models.Model):
    guess = models.CharField(max_length=100)
    
    def __str__(self):
	    return self.guess
    
    def get_absolute_url(self):
        return reverse('recall')
    