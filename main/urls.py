from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path("signup/<str:user_type>/",views.Signup,name="Signup"),
    path("request/create/",views.CreateRequest,name="CreateRequest"),
    path("login/",views.Login,name="Login"),
    path("requests/",views.GetRequests,name="GetRequests"),
    path("request/<int:request_id>/",views.GetRequest,name="GetRequest"),
    path("requests/",views.GetAllRequests,name="GetAllRequests"),
    path("request/assign-status/<int:request_id>/",views.AssignStatus,name="AssignStatus"),
    path("request/assign-designer/<int:request_id>/",views.AssignSolutionDesigner,name="AssignSolutionDesigner"),
    
    
]