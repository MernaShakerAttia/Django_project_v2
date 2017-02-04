from __future__ import unicode_literals

from django.db import models

from datetime import date


# Create your models here.
"""(#class users(models.Model):#)
	user_name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	when we got inetger  we treat it like string
	passwd=models.CharField(max_length=200)#)"""
class category(models.Model):
	title=models.CharField(max_length=200)

class Post(models.Model):
	title=models.CharField(max_length = 200)
	contant=models.TextField()
	post_category=models.ForeignKey(category,on_delete=models.CASCADE)
	user_reply=models.TextField()
	post_time=models.DateTimeField('datetime')
	


		


class forbidden(models.Model):
	rude_words=models.TextField()


	


