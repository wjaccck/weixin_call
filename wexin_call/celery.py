from __future__ import absolute_import
import os
from celery import Celery
from celery import Celery, platforms
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weixin_call.settings')

from django.conf import settings  # noqa
app = Celery('weixin_call')
platforms.C_FORCE_ROOT = True
# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
