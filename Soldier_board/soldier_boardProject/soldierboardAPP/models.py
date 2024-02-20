from django.db import models


class SBoard(models.Model):
    esm_no = models.IntegerField()
    esm_name = models.CharField(max_length=30)
    resident = models.CharField(max_length=20)
    service_no = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
