from django.db import models

# Create your models here.

class Device_Types(models.Model):
    device = models.CharField(max_length=150, primary_key=True)

    def __str__(self):
        return self.device


class AV(models.Model):
    hostname = models.CharField(max_length=100)
    device_type = models.ForeignKey('av_tracker.Device_Types', related_name='device_type')
    date_gen = models.DateTimeField(blank=False, null=False)
    date_rec = models.DateTimeField(blank=False, null=False)
    ip_address = models.CharField(max_length=15)
    username = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    organization = models.CharField(max_length=200)
    action = models.CharField(max_length=200)
    detection = models.CharField(max_length=200)
    logs = models.CharField(max_length=200)
    dat_version = models.CharField(max_length=20)
    filepath = models.TextField()
    comments = models.TextField()
    updating = models.BooleanField(default=False)
    created_by = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.hostname