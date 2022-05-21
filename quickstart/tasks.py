from celery.utils.log import get_task_logger

from newTex.celery import app
from .email import send_email

logger = get_task_logger(__name__)


@app.task
def send_email_task(username, email):
    send_email(username, email)
    logger.info(f'Username: {username} and email: {email}')
    return True
