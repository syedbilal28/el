from django.urls import path
from . import views
urlpatterns=[
    
    path("signup/<str:user_type>/",views.Signup,name="Signup"),
    path("request/create/",views.CreateRequest,name="CreateRequest"),
    path("login/",views.Login,name="Login"),
    path("user/requests/",views.GetRequestsUser,name="GetRequests"),
    path("request/<int:request_id>/",views.GetRequest,name="GetRequest"),
    path("requests/",views.GetAllRequests,name="GetAllRequests"),
    path("request/assign-status/<int:request_id>/",views.AssignStatus,name="AssignStatus"),
    path("request/assign-designer/<int:request_id>/",views.AssignSolutionDesigner,name="AssignSolutionDesigner"),
    path("designers/",views.GetSolutionDesigners,name="GetSolutionDesigners"),
    path("solution-designer/requests/",views.GetRequestsSolutionDesigner,name="SolutionDesignerRequests"),
    path("requests/assign/<int:request_id>/",views.AssignCostModel,name="AssignCostModel"),
    path("cost-models/",views.ReturnCostModels,name="ReturnCostModels"),
    path("get-comment/<int:request_id>/",views.GetComment,name="GetComment"),
    path("create-comment/",views.CreateComment,name="CreateComment")

    
]