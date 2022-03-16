import json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate
from .models import CostModel, Profile, Request
from .serializers import CostModelSerializer, ProfileSerializer, RequestSerializer, UserSerializer
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
def GetRequestsUser(request):
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
        request_obj=RequestSerializer(request_obj,data=data,partial=True)
        if request_obj.is_valid():
            request_obj.save()
        return JsonResponse(request_obj.data,safe=False)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def GetAllRequests(request):
    token=Token.objects.get(key=request.headers["Authorization"].split(" ")[-1])
    user=token.user
    if user.profile.status== "Demand Manager" or user.profile.status=="Manager":
        status_filter=request.GET.get("status")
        if status_filter:
            request_obj=Request.objects.filter(status=status_filter)
        else:
            request_obj=Request.objects.all()
        request_obj=RequestSerializer(request_obj,many=True)
        return JsonResponse(request_obj.data,safe=False)
    return HttpResponse(status=403)

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def AssignStatus(request,request_id):
    token=Token.objects.get(key=request.headers["Authorization"].split(" ")[-1])
    user=token.user
    if user.profile.status== "Demand Manager":
        data=json.loads(request.body)
        request_obj=Request.objects.get(pk=request_id)
        request_obj.status=data.get("status")
        request_obj.save()
        return HttpResponse(status=201)
    return HttpResponse(stauts=403)

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def AssignSolutionDesigner(request,request_id):
    token=Token.objects.get(key=request.headers["Authorization"].split(" ")[-1])
    user=token.user
    if user.profile.status== "Demand Manager":
        data=json.loads(request.body)
        request_obj=Request.objects.get(pk=request_id)
        solution_designer=Profile.objects.get(pk=int(data.get("designer")))
        request_obj.assigned_to=solution_designer
        request_obj.save()
        return HttpResponse(status=201)
    return HttpResponse(stauts=403)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def GetSolutionDesigners(request):
    token=Token.objects.get(key=request.headers["Authorization"].split(" ")[-1])
    user=token.user
    if user.profile.status== "Demand Manager":
        designers=Profile.objects.filter(status="Solution Designer")
        designers=ProfileSerializer(designers,many=True)
        return JsonResponse(designers.data,status=200)
    return HttpResponse(status=403)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def GetRequestsSolutionDesigner(request):
    token=Token.objects.get(key=request.headers["Authorization"].split(" ")[-1])
    user=token.user
    if user.profile.status== "Solution Designer":
        request_obj=Request.objects.filter(assigned_to=user.profile)
        request_obj=RequestSerializer(request_obj,many=True)
        return JsonResponse(request_obj.data,safe=False)
    return HttpResponse(status=403)

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def AssignCostModel(request,request_id):
    token=Token.objects.get(key=request.headers["Authorization"].split(" ")[-1])
    user=token.user
    if user.profile.status== "Solution Designer":
        data=json.loads(request.body)
        request_obj=Request.objects.get(pk=request_id)
        cost_model=CostModel.objects.get(name=data.get("cost_model"))
        request_obj.cost_model=cost_model
        request_obj.save()
        return HttpResponse(status=201)
    return HttpResponse(status=403)

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def ReturnCostModels(request):
    token=Token.objects.get(key=request.headers["Authorization"].split(" ")[-1])
    user=token.user
    if user.profile.status== "Solution Designer":
        cost_models=CostModel.objects.all()
        cost_models=CostModelSerializer(cost_models,many=True)
        return JsonResponse(cost_models.data,safe=False)
    return HttpResponse(status=403)








 



    
    







