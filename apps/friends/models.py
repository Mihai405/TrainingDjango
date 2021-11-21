from django.db import models
from apps.users.models import User

class Friend(models.Model):
    first_name      =   models.CharField(max_length=50)
    last_name       =   models.CharField(max_length=50)
    phone_number    =   models.CharField(max_length=10)
    user            =   models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name