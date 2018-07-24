
from django.db import models
from django.core.urlresolvers import reverse

class Item(models.Model):
    item_logo = models.FileField()
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField()
    item_status = models.CharField(max_length=40)
    phone = models.IntegerField(default=984)
    location = models.CharField(max_length=75, default='')
    seller_info = models.CharField(max_length=1000, default='')
    general_detail = models.CharField(max_length=1000, default='')
    description = models.CharField(max_length=1000)
    item_spec = models.CharField(max_length=500, default='')
    delivery = models.CharField(max_length=75)
    category = models.CharField(max_length=75)
    cid = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('mobiles:ad-conf',kwargs={'pk':self.pk})


    def __str__(self):
        return self.seller_info
