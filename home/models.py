# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Business(models.Model):

    #__Business_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    industry = models.CharField(max_length=255, null=True, blank=True)

    #__Business_FIELDS__END

    class Meta:
        verbose_name        = _("Business")
        verbose_name_plural = _("Business")


class Expense(models.Model):

    #__Expense_FIELDS__
    amount = models.BooleanField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Expense_FIELDS__END

    class Meta:
        verbose_name        = _("Expense")
        verbose_name_plural = _("Expense")



#__MODELS__END
