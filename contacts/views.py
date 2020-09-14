from django.shortcuts import render, redirect
from .models import Contact
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.contrib import messages
# Create your views here.


def contact(request):
    if request.method == 'POST':

        first_name = request.POST['firstname']
        print('first_name --- {}'.format(first_name))
        last_name = request.POST['lastname']
        print('last_name --- {}'.format(last_name))
        email = request.POST['email']
        print('email --- {}'.format(email))
        phone = request.POST['phone']
        print('mobile_number --- {}'.format(phone))
        msg = request.POST['message']
        print('message --- {}'.format(msg))
        has_contacted = Contact.objects.all().filter(
            email=email, first_name=first_name, last_name=last_name)
        if has_contacted:
            messages.error(
                request, 'You have Already made an inquiry')
            print("Error has been sended")
            return redirect('index')
        else:
            contact = Contact(first_name=first_name, last_name=last_name,
                              email=email, phone=phone, message=msg)
            print("Request been checked")
            contact.save()
            print("Request Saved")
        # Send Mail
        html_template = " We have got your message and will reach you soon"
        send_mail(
            'Thanks For Contacting us',
            'Hello, ' + first_name +
            html_template,
            'shivamrvgupta@gmail.com',
            [contact.email],
            fail_silently=False,
        )

        messages.success(
            request, 'Your request have been submitted, We will get back to you soon ')
        print("Message has been Sent")
        return redirect('index')
