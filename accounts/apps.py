from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    verbose_name = 'User Profiles'
    
    def ready(self):
        from . import signals