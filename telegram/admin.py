from django.contrib import admin
from . import models

admin.site.register(models.Adminlog)
admin.site.register(models.Channel)
admin.site.register(models.Chat)
admin.site.register(models.Chatparticipants)
admin.site.register(models.Forward)
admin.site.register(models.Media)
admin.site.register(models.Message)
admin.site.register(models.Resume)
admin.site.register(models.Resumeentity)
admin.site.register(models.Resumemedia)
admin.site.register(models.User)