from rest_framework import serializers
from .models import Application,Offer
class OffersSerializers(serializers.ModelSerializer):
    description  = serializers.CharField(allow_null=True)
    deadline  = serializers.DateTimeField(allow_null=True)
    start  = serializers.DateTimeField(allow_null=True)
    title = serializers.CharField(allow_null=True)
    class Meta:
        model = Offer
        fields = '__all__'
    


class ApplicationsSerializers(serializers.ModelSerializer):
   
    offer_title = serializers.CharField(allow_null=True)
    applicant_email = serializers.CharField(allow_null=True)
    applicant_name  = serializers.CharField(allow_null=True)
    date = serializers.TimeField(default=None,allow_null=True)
    status = serializers.CharField(max_length=100,default="unviewd")
    class Meta:
        model = Application
        fields = '__all__'


    
