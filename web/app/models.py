from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import EmailValidator, RegexValidator
from django.utils.translation import gettext_lazy as _





class Product(models.Model):
    name = models.CharField("Name", max_length=200 , blank=True)
    cost = models.FloatField("Cost", null=True, blank=True, default=0)
    sku = models.CharField("Sku", max_length=8, unique=True ,validators=[RegexValidator(regex='^.{8}$', message='8 characters required')])

    NO_CURRENCY = "NO_CURRENCY"
    EURO = "EURO"
    US_DOLLAR = "US_DOLLAR"
    BRITISH_POUND = "BRITISH_POUND"
    FIAT_CURRENCY_CHOICES = (
        (NO_CURRENCY, '-'),
        (EURO, 'EUR'),
        (US_DOLLAR, 'USD'),
        (BRITISH_POUND, 'GBP'),
    )

    fiat_currency = models.CharField("Fiat Currency",max_length=50, choices=FIAT_CURRENCY_CHOICES, default=EURO)


    def __str__(self):
        return self.name





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tokens_amount=models.IntegerField("Tokens Amount of User", default=0)

    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
