from django.apps import AppConfig
import logging


logger = logging.getLogger('core')


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
