from django.contrib import admin

from .models import *

admin.site.register(WizzerUser)
admin.site.register(Whiz)
admin.site.register(Like)
admin.site.register(Dislike)

