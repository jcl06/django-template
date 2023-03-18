from celery import shared_task, group
from celery.utils.log import get_task_logger
import time
logger = get_task_logger(__name__)

#celery -A configs worker -l info -P gevent -c 10
#celery -A configs purge
#celery -A configs beat -l info  --scheduler django_celery_beat.schedulers:DatabaseSchedule

@shared_task
def main(items):
    logger.info('Executing main task.')
    print('Executing main task.')
    out = single_child(items)
    print("final:", out)
    #if result.ready():
    #    print('celery status: {0}'.format(result.get()))


def single_child(items):
    logger.info('Executing Child!')
    #job = group(child.s(item) for item in items)
    #result = job.apply_async()
    for item in items:
        result = child.delay(item).get()
    print('celery status: {0}'.format(result))
    return 'celery status: {0}'.format(result)

def multiple_child(items):
    logger.info('Executing Child!')
    job = group(child.s(item) for item in items)
    result = job.apply_async()
    print('celery status: {0}'.format(result.get()))
    return 'celery status: {0}'.format(result.get())

@shared_task
def child(x):
    logger.info('Value: {0}'.format(x))
    print(('Executing Child!'))
    print('Value: {0}'.format(x))
    print(x)
    for i in range(10):
        print(i)
        time.sleep(1)
    return x