
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from forms import ContactForm
# Create your views here.

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
			