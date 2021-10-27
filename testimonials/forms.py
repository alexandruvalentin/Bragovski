from django import forms
from .models import Testimonials


class TestimonialsForm(forms.ModelForm):

    class Meta:
        model = Testimonials
        fields = ['full_name', 'comment', 'rate']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Name',
            'comment': 'Write your comment...',
            'rate': '0',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False
