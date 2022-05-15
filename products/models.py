from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .utils import generic_info_dict, send_transaction
import hashlib

class Lot(models.Model):
    lot_code = models.CharField(max_length=20)
    tracking_code = models.CharField(max_length=10)
    product = models.CharField(max_length=30)
    production_quantity = models.CharField(max_length=10)
    date_time_arrival = models.DateTimeField(default=timezone.now)
    date_time_production =models.DateTimeField(default=timezone.now)
    manufacturing_plant = models.CharField(max_length=30)
    recipient = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True)
    hash = models.CharField(max_length=64, blank=True, null=True)
    hash_lot = models.CharField(max_length=64, blank=True, null=True)
    hash_info = models.CharField(max_length=64, blank=True, null=True)
    tx_id = models.CharField(max_length=100, blank=True, null=True) 

    def __str__(self):
        return self.lot_code

    class Meta:
        verbose_name = "Lot"
        verbose_name_plural = "Lot"
        ordering = ['-date_time_production']

    def get_absolute_url(self):
        return reverse("lot_detail", kwargs={'pk':self.pk})

    def save(self):
        info = str(generic_info_dict(self))
        self.hash_lot = hashlib.sha256(self.lot_code.encode('utf-8')).hexdigest()
        self.hash_info = hashlib.sha256(info.encode('utf-8')).hexdigest()
        self.hash = self.hash_lot + "    " + self.hash_info
        self.tx_id = self.write_on_chain()
        super(Lot, self).save()

    def write_on_chain(self):
        return send_transaction(self.hash)
        