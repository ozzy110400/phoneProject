import requests
from django.core import serializers
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

from .models import Message
from .serializers import MessageSerializer
from .forms import NewPhoneForm


def home(request):
    return render(request=request, template_name='API/index.html')


def add_phone(request):
    if request.method == "POST":
        form = NewPhoneForm(request.POST)
        if form.is_valid():
            phone_number = request.POST.get('number')
            message_data = get_message(phone_number)
            response = requests.post(url='http://kazinfoteh.org:9507/api', data=message_data)
            print(response)
            return redirect('home')
    form = NewPhoneForm()
    return render(request=request, template_name='API/add_phone.html', context={'form': form})


def get_message(phone_number):
    message = Message.objects.create_message(phone_number=phone_number)
    setattr(message, 'action', 'sendmessage')
    setattr(message, 'username', 'egistic1')
    setattr(message, 'password', 'nE4UbF1Zh')
    setattr(message, 'messagetype', 'SMS:TEXT')
    setattr(message, 'originator', 'olzhas')
    setattr(message, 'messagedata', 'Test+message+Olzhas.')

    message.save()
    message_data = model_to_dict(message, fields=['action', 'username', 'password', 'recipient', 'messagetype',
                                             'originator', 'messagedata'])

    return message_data

