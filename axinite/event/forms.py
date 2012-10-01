from django import forms
from django.contrib.auth.models import User
from axinite.event.models import Share


class EventForm(forms.Form):
    """
    Event Creation Form
    """
    topic = forms.CharField(label = "Name:",max_length=80,\
                            required=True
                            )
    description = forms.CharField(label="Desciption:",widget=forms.Textarea(),\
                                  required=False)
    location = forms.CharField(label="Where",max_length=80,required=True)
    start = forms.DateTimeField(label="Starts",required=True)
    end = forms.DateTimeField(label="Ends",required=True)
    organizers = forms.ModelChoiceField(queryset=User.objects.all(),
                                        required=False,
                                        )
    share = forms.ModelChoiceField(queryset=Share.objects.all(),required=False)