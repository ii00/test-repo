from django.contrib import admin

from api.users.models import User, Appointment
# from api.users.models import UserProfile

admin.site.register(User)
admin.site.register(Appointment)
# admin.site.register(UserProfile)