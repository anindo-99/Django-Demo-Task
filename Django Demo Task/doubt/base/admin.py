from django.contrib import admin
from .models import Userprofile, Posts
from embed_video.admin import AdminVideoMixin

from .models import Youtube

# Register your models here.
admin.site.register((Userprofile, Posts))


class YoutubeAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Youtube, YoutubeAdmin)
