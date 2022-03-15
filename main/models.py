from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=300)
    department=models.CharField(max_length=100,null=True)
    requests=models.ManyToManyField("Request")
    phone=models.CharField(max_length=20,null=True)

class Attachment(models.Model):
    file=models.FileField()


class Request(models.Model):
    timestamp=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(Profile,on_delete=models.CASCADE)
    last_modified=models.DateTimeField(auto_now=True)
    name=models.CharField(max_length=256)
    description=models.CharField(max_length=5000)
    attachments=models.ManyToManyField(Attachment)
    status=models.CharField(max_length=256,default="In Progress")
    assigned_to=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,related_name="solution_designer")

class Feedback(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    comment=models.CharField(max_length=1024)




@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)