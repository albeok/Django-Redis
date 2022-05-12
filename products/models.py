from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .utils import generic_info_dict, send_transaction
import json
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
    tx_id = models.CharField(max_length=100, blank=True, null=True) 

    def __str__(self):
        return self.tracking_code

    class Meta:
        verbose_name = "Lot"
        verbose_name_plural = "Lot"

    def get_absolute_url(self):
        return reverse("lot_detail", kwargs={'pk':self.pk})

    def save(self):
        self.tx_id = self.write_on_chain()
        super(Lot, self).save()

    def write_on_chain(self):
        # self.generic_info = {
        #     "lot_code" : self.lot_code,
        #     "tracking_code" : self.tracking_code,
        #     "image" :str(self.image),
        #     "production_quantity" : str(self.production_quantity),
        #     "date_time_arrival" : str(self.date_time_arrival),
        #     "date_time_production" : str(self.date_time_production),
        #     "manufacturing_plant" : self.manufacturing_plant,
        #     "recipient" : self.recipient
        #     }
        info = generic_info_dict(self)
        #   self.hash = hashlib.sha256(generic_info_json.encode('utf-8')).hexdigest()
        return send_transaction(json.dumps(info))
        

    # def save(self):
    #     self.transaction_id = self.write_on_chain_json()
    #     super(Lot, self).save()

    # def write_on_chain_json(self):
    #     json_lot = {}
    #     json_lot["lot_code"] = self.lot_code
    #     json_lot["tracking_code"] = self.tracking_code
    #     json_lot["generic_info"] = self.generic_info
    #     json_lot["image"] = str(self.image)
    #     json_lot["production_quantity"] = str(self.production_quantity)
    #     json_lot["date_time_arrival"] = str(self.date_time_arrival)
    #     json_lot["date_time_production"] = str(self.date_time_production)
    #     json_lot["manufacturing_plant"] = str(self.manufacturing_plant)
    #     json_lot["recipient"] = str(self.recipient)
    #     return send_transaction_get_tx_id(json.dumps(json_lot))

