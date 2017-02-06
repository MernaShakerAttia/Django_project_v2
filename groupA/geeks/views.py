from django.shortcuts import render
from .models import category, Post
from django.http import HttpResponse ,HttpResponseRedirect

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from forms import ContactForm
# Create your views here.

def show_all_categorys(request):
	all_cat = category.objects.all()
	context = {'all_categorys': all_cat}
	return render(request, 'geeks/index.html' ,context)

def show_posts(request,id):
	all_post = Post.objects.filter(post_category=id)
	context = {'all_posts': all_post}
	return render(request, 'geeks/show_all_posts.html' ,context)

def details(request,id):
    post = Post.objects.get(id=id)
    context = {'spacific_post':post}
    return render(request, 'geeks/show_post.html' ,context)
def contact(renquest):
	if renquest.method == 'Post':
		form =ContactForm(renquest.Post)
		if form.is_valid():
			topic = form.clean_data['topic']
			message=form.clean_data['message']
			sender=form.clean_data.get['sender','noreply@example.com']
			send_mail(
				'Feedback from your site, topic: %s' % topic,
				message, sender,
				['administrator@example.com']

				)
			return HttpResponseRedirect('/contact/thanks')
	else:
			form=ContactForm()
	return render_to_response('contact.html',{'form':form})
			