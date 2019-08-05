from django.contrib import admin
from .models import Job, Skill, UserProfile, Categories


admin.site.register(Job)
admin.site.register(Skill)
admin.site.register(UserProfile)
admin.site.register(Categories)
