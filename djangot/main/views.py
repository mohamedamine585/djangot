from django.shortcuts import render
from django.http import JsonResponse
from .models import Application,Offer
from .serializers import ApplicationsSerializers,OffersSerializers
from rest_framework.response import  Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def apps_list(response):
    try:     
       apps = Application.objects.all()
       S = ApplicationsSerializers(apps,many=True)
       return Response(S.data)
    except:
       return JsonResponse({"status":"NONE"})

@api_view(['POST'])
def post_offer(response):
    try:
       serializer = OffersSerializers(data= response.data)
       if(serializer.is_valid()):
           serializer.save()
           return JsonResponse(data={"status":"OK"},safe=False)
       else:
          return JsonResponse(data={"status":"NONE"},safe=False)
    except:
        return JsonResponse(data={"status":"NONE"},safe=False)

@api_view(['GET'])
def offers_list(response):
    try:
       offers = Offer.objects.all()
       S = OffersSerializers(offers,many=True)
       return Response(S.data)
    except :
        return JsonResponse({"status":"NONE"})

@api_view(['POST'])
def post_app(response):
    try:
       serializer = ApplicationsSerializers(data= response.data)
       if(serializer.is_valid()):
          serializer.save()
          return JsonResponse(data={"status":"OK"},safe=False)
       else :
          return JsonResponse(data={"status":"NONE"},safe=False)
    except:
        return JsonResponse(data={"status":"NONE"},safe=False)

@api_view(['DELETE'])
def delete_app(response,idapp):
    try:
      app = Application.objects.get(id = idapp)
      app.delete()
      return JsonResponse(data={"status":"OK"},safe=False)
    except:
        return JsonResponse(data={"status":"NONE"},safe=False)