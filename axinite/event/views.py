#-------------------- Axinite Imports ----------------------#
from django.shortcuts import render_to_response
from django.template import RequestContext
#-------------------- Axinite Imports ----------------------#
from axinite.event.models import Share, Event
from axinite.event.forms import EventForm
#-------------------- Axinite Imports ----------------------#


def eventcreation(request):
    """
    User will create the event through this form.
    """
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['start'].widget.attrs['class'] = "datepicker"
        self.fields['end'].widget.attrs['class'] = "datepicker"
        categories = Share.objects.all()
        self.fields['category'].choices = [(c.pk,c.type) for c in categories]
        
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
                                share_with = cd['share'],
                                organizer = request.user
                                )
            
        else:
            print "EventForm is Invalid"
    else:
        
        event_form = EventForm()
        if request.GET.get('id'):
            id = request.GET['id']
            event_obj = Event.objects.get(id=id)
            
            try:
                event_form.fields['topic'].initial = event_obj.topic
            except:
                pass
            try:
                event_form.fields['description'].initial = event_obj.description
            except:
                pass
            try:
                event_form.fields['location'].initial = event_obj.location
            except:
                pass
            try:
                event_form.fields['organizer'].initial = event_obj.organizer
            except:
                pass
            try:
                event_form.fields['start'].initial = event_obj.start
            except:
                pass
            try:
                event_form.fields['end'].initial = event_obj.end
            except:
                pass
            try:
                event_form.fields['share'].initial = event_obj.share_with
            except:
                pass
#            try:
#                event_form.fields['event_poster'].initial = event_obj.
#            except:
#                pass
            
            
    return render_to_response('event/create_event.html',
                              {'eventform':event_form},
                              context_instance = RequestContext(request)
                              )          
        