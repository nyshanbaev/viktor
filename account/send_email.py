from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'Viktor',
        f'http://localhost:8000/account/activate/{code}/',
        'baitikovskij@gmail.com',
        [email]
    )