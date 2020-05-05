from django.db import models
from django.contrib.auth.models import User

class AllLogin(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    logInTime = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.user) + ': ' + str(self.logInTime)

# Create your models here.
# class AllLogout(models.Model):
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
#     logOutTime = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return str(self.user) + ': ' + str(self.logOutTime)