from datetime import datetime
from locale import currency
from pyexpat import model
from statistics import mode
from telnetlib import STATUS
from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()

NG = 'NG'
GH = 'GH'
UK = 'UK'
currency_type = [(NG,'NG'),(GH,'GH'),(UK,'UK')]

pending = 'pending'
successful = 'successful'
declined = 'declined'
transaction_status = [(pending,'pending'),(successful,'successful'),(declined,'declined'),]

class users_wallet(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=20)
    credict_ballance = models.CharField(max_length=20)
    Currency = models.CharField(max_length=20, choices=currency_type)
    Billing_Address = models.CharField(max_length=100, null=True, blank=True)

class transaction(models.Model):
    user = models.CharField(max_length=20)
    Sender = models.CharField(max_length=20)
    amount = models.CharField(max_length=20)
    Currency = models.CharField(max_length=20, choices=currency_type)
    status = models.CharField(max_length=12, choices=transaction_status)
    transaction_date = models.DateTimeField(auto_now_add=True)   

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return  str(self.user) +"~" + str(self.phone_number) + '~'+ str(self.date_created)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)
    instance.profile.save()
    
class rate(models.Model):
    Naira = models.IntegerField()
    Cedes = models.IntegerField()
    