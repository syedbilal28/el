import json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate
from .models import Profile, Request
from .serializers import ProfileSerializer, RequestSerializer, UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes,permission_classes,api_view
from rest_framework.authtoken.models import Token
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def Login(request):
    body=json.loads(request.body)
    email=body.get("email")
    password=body.get("password")
    user=authenticate(request,username=email,password=password)
    if user:
        token=user.token
        return JsonResponse({"token":token.key})
    return HttpResponse(status=404)
@csrf_exempt
def Signup(request,user_type):
    body=json.loads(request.body)
    user=UserSerializer(data=body)
    if user.is_valid():
        user=user.save()
    profile=Profile.objects.create(user=user,phone=body.get("phone"),status=user_type,department=body.get("department"))

    return HttpResponse(status=201)
@csrf_exempt
@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def CreateRequest(request):
    body=json.loads(request.body)
    token=Token.objects.get(key=request.headers["Authorization"].split(" ")[-1])
    user=token.user    
    body["created_by"]=user.profile.pk
    print(body)
    request_obj=RequestSerializer(data=body)
    if request_obj.is_valid():
        request_obj.save()
        return HttpResponse(status=201)
    return HttpResponse(status=403)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def GetRequests(request):
    token=Token.objects.get(key=request.headers["Authorization"].split(" ")[-1])
    user=token.user
    request_objs=Request.objects.filter(created_by=user.profile)
    request_objs=RequestSerializer(request_objs,many=True)
    return JsonResponse(request_objs.data,safe=False)

@api_view(["GET","PUT"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def GetRequest(request,request_id):    
    if request.method == "GET":
        request_obj=Request.objects.get(pk=request_id)
        request_obj=RequestSerializer(request_obj)
        return JsonResponse(request_obj.data,safe=False)
    elif request.method == "PUT":
        data=json.loads(request.body)
        request_obj=Request.objects.get(pk=request_id)
        request_obj=RequestSerializer(request_obj)
        request_obj.update(data=data)
        return JsonResponse(request_obj.data,safe=False)





