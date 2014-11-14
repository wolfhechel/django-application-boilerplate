from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DefaultApplication(AppConfig):

    name = '{{app_name}}'

    verbose_name = _('{{app_name}}')

    def ready(self):
        from . import conf, signals