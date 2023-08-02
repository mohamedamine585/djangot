from django.shortcuts import render
from django.http import JsonResponse
from .models import Application,Offer
from .serializers import ApplicationsSerializers,OffersSerializers
from rest_framework.response import  Response
from rest_framework.decorators import api_view


# get the applications lsit
@api_view(['GET'])
def apps_list(response):
    try:     
       apps = Application.objects.all()
       S = ApplicationsSerializers(apps,many=True)
       return Response(S.data)
    except:
       return JsonResponse({"status":"NONE"})


# post  an offer ...
@api_view(['POST'])
def post_offer(response):
    try:
       serializer = OffersSerializers(data= response.data)
       if(serializer.is_valid()):
           serializer.save()
           return JsonResponse(data={"status":"OK"},safe=False)
       else:        
        print(serializer.errors)

        return JsonResponse(data={"status":"NONE"},safe=False)
    except:
        return JsonResponse(data={"status":"NONE"},safe=False)


# get the offers list ...
@api_view(['GET'])
def offers_list(response):
    try:
       offers = Offer.objects.all()
       S = OffersSerializers(offers,many=True)
       return Response(S.data)
    except :
        return JsonResponse({"status":"NONE"})



#post an application ... 
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


# delete an application
@api_view(['DELETE'])
def delete_app(response,idapp):
    try:
      app = Application.objects.get(id = idapp)
      
      app.delete()
      return JsonResponse(data={"status":"OK"},safe=False)
    except:
        return JsonResponse(data={"status":"NONE"},safe=False)
    
# accept application ...
@api_view(['PUT'])
def accept_app(response,idapp):
    try:
      app = Application.objects.get(id = idapp)
      app.status = "accepted"
      app.save()
      return JsonResponse(data={"status":"OK"},safe=False)
    except:
        return JsonResponse(data={"status":"NONE"},safe=False)