from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from api.celery import app
from users.models import User


@app.task
def new_order_task(user_id, **kwargs):
    """
    Отправляем письмо при изменении статуса заказа
    """
    # send an e-mail to the user
    user = User.objects.get(id=user_id)

    msg = EmailMultiAlternatives(
        # title:
        "Обновление статуса заказа",
        # message:
        'Заказ сформирован',
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [user.email]
    )
    msg.send()
