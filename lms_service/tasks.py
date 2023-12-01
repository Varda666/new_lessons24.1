from django.conf import settings
from django.core.mail import send_mail


def _send_mail_email(recipient_list):
    send_mail(
        subject='Обновление курса',
        message=f'Курс, на который вы подписаны, обновлен.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[recipient_list]
    )

