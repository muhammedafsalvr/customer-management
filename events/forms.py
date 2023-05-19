from django import forms
from django.forms import TextInput, Select, DateInput

from events.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

        widgets = {
            'title': TextInput(attrs={'class':'required input'}),
            'event_type': Select(attrs={'class':'required input'},choices=Event.CHOICES),
            'event_date': DateInput(attrs={'class':'required input', 'type':'date'}, format="%Y-%m-%dT%H:%M"),
        }
        
