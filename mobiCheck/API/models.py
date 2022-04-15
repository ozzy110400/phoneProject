from django.core.validators import RegexValidator
from django.db import models


class Phone(models.Model):
    number_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Enter a valid number')
    number = models.CharField(validators=[number_validator], max_length=17)


class MessageManager(models.Manager):
    def create_message(self, phone_number):
        message = self.create(recipient=phone_number)

        return message


class Message(models.Model):
    action = models.CharField(max_length=15, blank=True)
    username = models.CharField(max_length=15, blank=True)
    password = models.CharField(max_length=15, blank=True)
    recipient = models.CharField(max_length=15, blank=True)
    messagetype = models.CharField(max_length=15, blank=True)
    originator = models.CharField(max_length=15, blank=True)
    messagedata = models.CharField(max_length=255, blank=True)

    objects = MessageManager()
