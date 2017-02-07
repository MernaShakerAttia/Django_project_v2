from django import forms
#from .models import ContactForm
TOPIC_CHOICES = (
('general', 'General enquiry'),
('bug', 'Bug report'),
('suggestion', 'Suggestion'),
)

class ContactForm(forms.Form):
	topic = forms.ChoiceField(choices=TOPIC_CHOICES)
	message = forms.CharField()
	sender = forms.EmailField(required=False)

""" for validation email to check many word to send """

def clean_message(self):
	message = self.clean_data.get('message', '')
	num_words = len(message.split())
	if num_words < 4:
		raise forms.ValidationError("Not enough words!")
	return message	