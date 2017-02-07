from __future__ import unicode_literals

from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class useres(models.Model):
	user_name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	passwd=models.CharField(max_length=200)


class category(models.Model):
	title=models.CharField(max_length=200)
	#post_time=models.DateTimeField('datetime')
	#contant=models.TextField()
	def was_published_recently(self):
 		return date.today() > self.post_time.date()

	was_published_recently.short_description = 'Puplished Before Today ?'
 	was_published_recently.boolean = True

	def __str__(self):
		return self.title

class Post(models.Model):
	title=models.CharField(max_length = 200)
	contant=models.TextField()
	post_category=models.ForeignKey(category,on_delete=models.CASCADE)
	post_time=models.DateTimeField('datetime')
	post_image = models.ImageField(upload_to = 'geeks/static/imgs/',default='No_image_available.svg')
	
	def __str__(self):
		return '%s %s'%(self.title, self.post_category)

	def was_published_recently(self):
 		return date.today() > self.post_time.date()

	was_published_recently.short_description = 'Puplished Before Today ?'
 	was_published_recently.boolean = True

	
class Comment(models.Model):
	comment_contant=models.TextField()
	comment_date=models.DateTimeField('datetime')
	user_reply=models.TextField()
	post_comment_id=models.ForeignKey(Post,on_delete=models.CASCADE)

# class Subscribe(models.Model):
# 	user_id=models.ForeignKey('User')
# 	category=models.ForeignKey(category,on_delete=models.CASCADE)

class forbidden(models.Model):
	rude_words=models.TextField()
	def __str__(self):
		return self.rude_words
	