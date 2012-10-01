#-------------------- Axinite Imports ----------------------#
from django.shortcuts import render_to_response
from django.template import RequestContext
#-------------------- Axinite Imports ----------------------#
from axinite.event.models import *
from axinite.event.forms import EventForm
#-------------------- Axinite Imports ----------------------#


def eventcreation(request):
    """
    User will create the event through this form.
    """
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['date_started4'].widget.attrs['class'] = "datepicker"
        self.fields['date_completed4'].widget.attrs['class'] = "datepicker"
        self.fields['date_started5'].widget.attrs['class'] = "datepicker"
        self.fields['date_completed5'].widget.attrs['class'] = "datepicker"
        categories = Category.objects.all()
        self.fields['category'].choices = [(c.pk,c.type) for c in categories]
        self.fields['category'].widget.attrs['class'] = "category_class"
        self.fields['category'].widget.attrs['style'] = "width: 100px"
        
    if request.method == "POST":
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            cd = event_form.cleaned_data
            event_obj,created = Event.objects.get_or_create(
                                topic = cd['topic'],
                                description = cd['description'],
                                start = cd['start'],
                                end = cd['end'],
                                location = cd['location'],
                                organizers = request.user,
                                share = cd['share'],
                                )
        else:
            print "EventForm is Invalid"
    else:
        event_form = EventForm()
    return render_to_response('event/create_event.html',
                              {'eventform':event_form},
                              context_instance = RequestContext(request)
                              )          
        