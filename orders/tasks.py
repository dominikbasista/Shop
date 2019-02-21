# from celery import task
# from django.core.mail import send_mail
# from .models import Order
#
#
# @task
# def order_created(order_id):
#     order = Order.objects.get(id=order_id)
#     subject = "Zamówienie nr {}".format(order_id)
#     message = 'Witaj {}\n Właśnie złożyłeś zamowienie.'\
#               'Numer Twojego zamówienia to {}'.format(order.first_name, order_id)
#
#     mail_sent = send_mail(subject, message, 'schlomodichstein@gmail.com', [order.email])
#
#     return mail_sent

