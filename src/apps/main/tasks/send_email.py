from django.core.mail import EmailMessage


def send_email(subject, body, from_email, to_list, fail_silently, headers = None):
    email = EmailMessage(
        subject = subject, body = body, from_email = from_email, to = to_list, headers = headers
    )
    email.content_subtype = 'html'
    email.send(fail_silently = fail_silently)
    return True
