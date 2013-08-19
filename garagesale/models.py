from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    price = models.FloatField()
    main_view = models.TextField()
    sold = models.BooleanField(default=False)
    partner = models.CharField(max_length=30, blank=True, default='')

class Screenshots(models.Model):
    url = models.TextField()
    item = models.ForeignKey(Item, related_name='screenshots')


class ContactRequest(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    message = models.TextField()
    item = models.ForeignKey(Item, related_name='requests')
    