from django.apps import AppConfig


class UserAppConfig(AppConfig):
    name = "user"
    verbose_name = "User"

    # def ready(self):
    #     import user.signals
