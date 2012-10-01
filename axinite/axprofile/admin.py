#from django.contrib import admin
#from django.contrib import admin
#from axinite.axprofile.models import UserFriends
#from axinite.axprofile.models import Country,State,City, CourseType,\
#EducationHistory,EmploymentHistory
#from axinite.axusers.models import UserProfile
#
#
#class CountryAdmin(admin.ModelAdmin):
#    list_display = ('name',)
#    
#
#class StateAdmin(admin.ModelAdmin):
#    list_display = ("name","country")
#    
#
#class CityAdmin(admin.ModelAdmin):
#    list_display = ("name","state","country")
#    
#    
#class UserProfileAdmin(admin.ModelAdmin):
#    list_display = ("user","gender","birthdate","user")
#    
#
#class EmploymentHistoryAdmin(admin.ModelAdmin):
#    list_display = ("company_name","date_of_joining","date_of_leaving","position")
#    
#
#class EducationHistoryAdmin(admin.ModelAdmin):
#    list_display = ("user","course_type","institute_name","qualification_level","year_of_passout")
#    
#
#class CourseTypeAdmin(admin.ModelAdmin):
#    list_display = ("name",)
#    
#
#class UserFriendsAdmin(admin.ModelAdmin):
#    list_display = ("user","friend_name","social_site")
#    
#admin.site.register(UserFriends,UserFriendsAdmin)
#admin.site.register(Country,CountryAdmin)
#admin.site.register(State,StateAdmin)
#admin.site.register(City,CityAdmin)
#admin.site.register(UserProfile,UserProfileAdmin)
#admin.site.register(CourseType,CourseTypeAdmin)
#admin.site.register(EducationHistory,EducationHistoryAdmin)
#admin.site.register(EmploymentHistory,EmploymentHistoryAdmin)
