from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import *

class PictureAdmin(admin.ModelAdmin):
    list_display = ('id','photo',)
    list_display_links = ('id','photo')
    search_fields = ('photo',)
admin.site.register(PictureHome,PictureAdmin)