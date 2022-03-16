from django.contrib import admin
from .models import CostModel, Request,Profile,Feedback
# Register your models here.
admin.site.register(Request)
admin.site.register(Profile)
admin.site.register(Feedback)
admin.site.register(CostModel)