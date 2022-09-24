from django.contrib.admin import site

from user.models import User

site.register(User)
