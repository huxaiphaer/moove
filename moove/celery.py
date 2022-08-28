from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moove.settings')
app = Celery('moove')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.beat_schedule = {
    "populate_vehicles": {
        "task": "reports.tasks.populate_vehicles",
        "schedule": crontab(minute="*/1"),
    },
    "debug_task": {
        "task": "moove.celery.debug_task",
        "schedule": crontab(minute="*/1"),
    }
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
