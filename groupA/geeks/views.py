from django.shortcuts import render
from .models import category, Post
from django.http import HttpResponse ,HttpResponseRedirect
from datetime import date
from .forms import PostFrom
from django.contrib import auth
from django.contrib.auth.models import User
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

	#CRUD for user

def Post_new(request):
	
	form= PostFrom()
	if request.method == 'POST':
		form = PostFrom(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/geeks/allcategorys')
	context={'pnew_form':form}
	return render(request, 'geeks/Post_form.html', context)

def Posts_delete(request, id):

	p=Post.objects.get(pk=id)
	p.delete()
	return HttpResponseRedirect('/geeks')

def Post_update(request, id):
	P = Post.objects.get(pk=id)
	form = PostFrom(instance = q)
	if request.method == 'POST':
		form = PostFrom(request.POST, instance=q)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/geeks')



	context = {'pnew_form': form}
	return render(request, 'geeks/Post_form.html',context)

#////// for autho 

"""def login(request):
	user_name = request.POST['user_name']
	passwd = request.POST['passwd']
	user = auth.authenticate(user_name=username, passwd=password)
	if user is not None and user.is_active:
	# Correct password, and the user is marked "active"
		auth.login(request, user)
	# Redirect to a success page.
		return HttpResponseRedirect("/account/loggedin/")
	else:
	# Show an error page
		return HttpResponseRedirect("/account/invalid/")

#for logo out
def logout(request):
	auth.logout(request)
	# Redirect to a success page.
	return HttpResponseRedirect("/account/loggedout/")


	#  regestrion
def register(request):
	form = UserCreationForm()
	if request.method == 'POST':
		data = request.POST.copy()
		errors = form.get_validation_errors(data)
		if not errors:
			new_user = form.save(data)
			return HttpResponseRedirect("/books/")
	else:
		data, errors = {}, {}
		return render_to_response("registration/register.html", {
		'form' : forms.FormWrapper(form, data, errors)
})"""

#class admin(request):
#creating username
def create_user(request,user,email_id,password):
	#if request.method== 'POST'
	user = User.objects.create_user(user_name=user,
		email=email_id,
		passwd=password)
	user.is_superuser=True
	user.is_staff = True
	user.save()

def update(request):
	if request.method == 'POST':
		form = updateForm(data=request.POST, instance=request.user)
		update = form.save(commit=False)
		update.user = request.user
		update.save()
	else:
		form = updateForm(instance=request.user)

		return render(request, 'profile.html', {'form': form})

def set_password(request,user, password):
	user = User.objects.get(user_name=user)
	user.set_password(passwd)
	user.save()

def del_user(request, username):    
	try:
		u = User.objects.get(user_name = username)
		u.delete()
		messages.sucess(request, "The user is deleted")            

	except User.DoesNotExist:
		messages.error(request, "User doesnot exist")    
		return render(request, 'front.html')

	except Exception as e: 
		return render(request, 'front.html',{'err':e.message})

	return render(request, 'front.html')





