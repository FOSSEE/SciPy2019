from django.contrib import admin
from .models import CFP, RegistrationDetail

class CFPAdmin(admin.ModelAdmin):
	list_display = ['start_date','end_date','date_of_announcement']

class RegistrationDetailAdmin(admin.ModelAdmin):
	list_display = ['registration_type', 'start_date', 'end_date', 'registration_ticket','registration_description']		

admin.site.register(CFP, CFPAdmin)
admin.site.register(RegistrationDetail, RegistrationDetailAdmin)
