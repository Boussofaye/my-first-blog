from django.contrib import admin

# Register your models here.
from.models import Article
admin.site.register(Article)

from.models import UserProfile
admin.site.register(UserProfile)

