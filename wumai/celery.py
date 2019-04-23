from __future__ import absolute_import
import os
from datetime import timedelta
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wumai.settings')
app = Celery('wumai')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    CELERYBEAT_SCHEDULE={
        'get_data': {
            'task': 'data.tasks.get_data',
            'schedule': timedelta(hours=2),
        }
    }
)
