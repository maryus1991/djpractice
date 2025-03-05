from celery import shared_task


@shared_task(queue='tasks')
def send_email():
    print('sending email')
