from django.contrib import admin
from axinite.event.models import Event, Share, Comment, ReportAbuse, \
Participant, Organizer, Subscriber, SpamComment


class ShareAdmin(admin.ModelAdmin):
    list_display = ("id",'name')

admin.site.register(Share,ShareAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('topic','start','end','location')
    list_filter = ['location','start','end']
    search_fields = ['topic']

admin.site.register(Event,EventAdmin)

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("id",'event',)
    
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ("id",'event',)

admin.site.register(Organizer,OrganizerAdmin)
    
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("id",'event',)
    
admin.site.register(Subscriber,SubscriberAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('title','status','ratings')
    
admin.site.register(Comment,CommentAdmin)

class ParticiapantAdmin(admin.ModelAdmin):
    list_display = ("id",'event',)

admin.site.register(Participant,ParticipantAdmin)

class ReportAbuseAdmin(admin.ModelAdmin):
    list_display = ('reported_by','reported')
    
admin.site.register(ReportAbuse,ReportAbuseAdmin)

class SpamCommentAdmin(admin.ModelAdmin):
    list_display = ("event","reported")
    
admin.site.register(SpamComment,SpamCommentAdmin)