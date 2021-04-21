from django.db import models

class Voucher(models.Model):
    id = models.AutoField(primary_key=True)
    code=models.CharField(max_length=10)
    amount= models.FloatField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    redeemed = models.BooleanField(default=False)
    assigned =models.BooleanField(default=False)

class contact(models.Model):
    id = models.AutoField(primary_key=True)
    #mob = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    mobile = models.IntegerField()