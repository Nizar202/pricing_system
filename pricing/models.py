# pricing/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def get_default_admin():
    return User.objects.first().id  # استخدام أول مستخدم كقيمة افتراضية

class Offer(models.Model):
    association_name = models.CharField(max_length=100)
    client_address = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)  # تعيين التاريخ الافتراضي باستخدام timezone.now
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=get_default_admin)

    def __str__(self):
        return f"{self.association_name} - {self.date}"

class OfferItem(models.Model):
    offer = models.ForeignKey(Offer, related_name='items', on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def save(self, *args, **kwargs):
        self.total = self.price * self.quantity
        super().save(*args, **kwargs)
