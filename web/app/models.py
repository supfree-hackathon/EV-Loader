from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from django.utils.translation import gettext_lazy as _





class User(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="first name")
    last_name = models.CharField(max_length=50, verbose_name="last name")
    email = models.EmailField(
        _('email address'), 
        unique=True,
        blank=False,
        validators=[EmailValidator],
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )


    def __str__(self):
        return self.first_name + self.last_name 





class Product(models.Model):
    name = models.CharField("Name", max_length=200 , blank=True)
    cost = models.FloatField("Cost", null=True, blank=True, default=0)
    sku = models.CharField("Sku", max_length=8, unique=True ,validators=[RegexValidator(regex='^.{8}$', message='8 characters required')])


    def __str__(self):
        return self.name