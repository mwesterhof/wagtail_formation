from django.apps import AppConfig
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class FormationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'formation'

    def ready(self):
        migration_override = getattr(settings, 'MIGRATION_MODULES', {}).get('formation')
        if not migration_override:
            raise ImproperlyConfigured('formation needs to be added to a MIGRATION_MODULES setting')
