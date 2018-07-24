from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    location =models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100, default='')
    phone=models.IntegerField(default=0)
    website=models.URLField(default='')
    def __str__(self):
        return self.user.username



def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile =UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)