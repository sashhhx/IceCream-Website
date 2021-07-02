from api import serializers
from home.models import Contact
from django.shortcuts import render
from home.models import Contact
from api.serializers import ContactSerializer
from django.http import JsonResponse

# Create your views here.

def contact_detail(request):
    cont = Contact.objects.get(id=1)
    serializer = ContactSerializer(cont)
    return JsonResponse(serializer.data)

def contact_detail_list(request):
    cont = Contact.objects.all()
    serializer = ContactSerializer(cont, many=True)
    return JsonResponse(serializer.data, safe=False)

