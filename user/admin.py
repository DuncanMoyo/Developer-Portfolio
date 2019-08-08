from django.contrib import admin
from .models import Job, Skill, Categories, Achievements  # UserProfile


admin.site.register(Job)
admin.site.register(Skill)
# admin.site.register(UserProfile)
admin.site.register(Categories)
admin.site.register(Achievements)
