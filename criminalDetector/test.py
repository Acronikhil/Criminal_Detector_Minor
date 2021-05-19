from django.core.mail import send_mail

send_mail(
    'Test Mail',
    'This is test that how to send mail using django',
    '20.nikhildubey@gmail.com',
    ['otherworkneeds@gmail.com'],
    fail_silently=False,
)
