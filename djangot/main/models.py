from django.db import models
import bson
class Offer(models.Model):
    description = models.CharField(max_length=500)
    start = models.DateTimeField(max_length=400)
    deadline  = models.DateTimeField(max_length=400)
    title = models.CharField(max_length=400)
    status = models.CharField(max_length = 100)
    class Meta :
        db_table = "offers"
    
    def get_offers(self):
        offers = Offer.objects.all().filter(status="unviewd")
        return offers



  

class Application(models.Model):
    offer_title = models.CharField(max_length=100)
    applicant_name = models.CharField(max_length=200)
    applicant_email = models.CharField(max_length=300)
    date = models.TimeField(default=None)
    status = models.CharField(max_length=100,default="unviewd")
    class Meta :
        db_table = "applications"
        
    def __str__(self) -> str:
        return self.applicant_name
  