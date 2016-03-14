from django import forms

from .models import Panda


class BasicForm(forms.Form):
    SHIRT_CHOICES = [
        # <option value='S'>Small</option>
        ('S', 'Small'),
        ('M', 'Medium'),
    ]

    TECH_CHOICES = [
        (0, 'Python'),
        (1, 'Django'),
    ]

    name = forms.CharField(initial='Your name:')
    email = forms.EmailField()
    website = forms.URLField(initial='http://')
    comment = forms.CharField(help_text='Your opinion',
                              widget=forms.Textarea)
    subscribe = forms.BooleanField(initial=True)

    shirt_size = forms.ChoiceField(SHIRT_CHOICES)
    technologies = forms.MultipleChoiceField(TECH_CHOICES)


class PandaForm(forms.ModelForm):
    class Meta:
        model = Panda
        fields = '__all__'
