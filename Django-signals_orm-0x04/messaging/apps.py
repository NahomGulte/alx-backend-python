from django.apps import AppConfig

class ChatAppConfig(AppConfig):  # Replace with your actual app name
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'your_app_name'

    def ready(self):
        import your_app_name.signals  # Replace with your app name
