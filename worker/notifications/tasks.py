from celery import shared_task

@shared_task
def send_email():
    print('hello celery')


@shared_task
def ai_proccess():
    print('ai_proccess')