from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	#date_Posted = models.DateTimeField(auto_now_add=True)
	date_Posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User,on_delete=models.CASCADE)

def __str__(self):
	return self.title