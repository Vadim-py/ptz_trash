from django.forms import ModelForm
from django.forms import Textarea, TextInput, URLInput
from .models import Contact


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['first_name', 'message']
        widgets = {
            'message': Textarea(
                attrs={
                    'class': 'uk-textarea uk-form-small',
                    'placeholder': 'Напишите тут ваше сообщение'
                }
            ),
            'first_name': TextInput(
            attrs= {
                    'class': 'uk-textarea uk-form-small'
                }
            )
        }