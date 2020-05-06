from django.contrib import admin
from accounts.models import AllLogin, helpStatistics

# Register your models here.
admin.site.register(AllLogin)
# admin.site.register(AllLogout)
admin.site.register(helpStatistics)