from django.contrib import admin
from .models import Bucketlist

# from rest_framework.authtoken.admin import TokenAdmin


admin.site.site_header = 'Панель администратора'

# TokenAdmin.raw_id_fields = ('user',)

class BucketlistAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner')

admin.site.register(Bucketlist)