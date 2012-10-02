# Django imports
from django.contrib import admin
#axinite imports
from axinite.jobs_classifieds.models import JobsClassified, JobClassifiedSubscriber,\
JobsClassifiedsReplies



class JobsClassifiedAdmin(admin.ModelAdmin):
    list_display = ("job_start","job_end","owner",)
    
admin.site.register(JobsClassified,JobsClassifiedAdmin)

class JobClassifiedSubscriberAdmin(admin.ModelAdmin):
    list_display = ("jobs",)
    
admin.site.register(JobClassifiedSubscriber,JobClassifiedSubscriberAdmin)

class JobsClassifiedsRepliesAdmin(admin.ModelAdmin):
    list_display = ("jobs",)
    
admin.site.register(JobsClassifiedsReplies,JobsClassifiedsRepliesAdmin)