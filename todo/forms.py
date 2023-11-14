from django import forms
from .models import User

LEVEL = [
    (1, 'Low'),
    (2, 'Medium'),
    (3, 'High')
]


class TodoForm(forms.Form):
    user = forms.ChoiceField(
        choices=[(user.id, user.username) for user in User.objects.all()]
    )
    title = forms.CharField(
        required=True,
        max_length=64,
        error_messages={'required': 'Please enter a title.'}
    )
    description = forms.CharField(
        max_length=256,
        widget=forms.Textarea,
        error_messages={'required': 'Please enter a description.'}
    )
    necessary_time = forms.BooleanField(
        required=False,
        initial=True
    )
    level = forms.ChoiceField(
        choices=LEVEL
    )
