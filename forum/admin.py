from django.contrib import admin
from .models import Thread, ThreadReply

# Register your models here.
admin.site.register(Thread)
admin.site.register(ThreadReply)
