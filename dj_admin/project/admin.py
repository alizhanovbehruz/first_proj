from django.contrib import admin
from .models import Creator, author, channel

# Register your models here.

admin.site.register((Creator, author, channel))
