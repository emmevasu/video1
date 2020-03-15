from django.contrib import admin
from .models import Video

class AdminVideo(admin.ModelAdmin):
    class Meta:
        fields='__all__'
admin.site.register(Video,AdminVideo)



# Register your models here.
