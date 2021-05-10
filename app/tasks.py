from celery import shared_task
from celery_progress.backend import ProgressRecorder

from time import sleep

@shared_task(bind=True)
def go_to_sleep(self, duration):
    progress_recoder = ProgressRecorder(self)
    for i in range(50):
        sleep(duration)
        progress_recoder.set_progress(i+1, 50, f'On progress {i}')
    return 'Done'