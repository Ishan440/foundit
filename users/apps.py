from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
        # This may seem bizarre but django documentation recommends this way.
        