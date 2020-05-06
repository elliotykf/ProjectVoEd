from django.db import models
from django.contrib.auth.models import User

class AllLogin(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    logInTime = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.user) + ': ' + str(self.logInTime)


class helpStatistics(models.Model):
    customerType = (
        ('Student', 'Student'),
        ('Instructor', 'Instructor'),
        ('Other', 'Other')
    )
    customer = models.CharField(max_length = 200, null = True, choices = customerType)

    helpType = (
        ('Software', 'Software'),
        ('Hardware', 'Hardware'),
        ('Other', 'Other')
    )
    help = models.CharField(max_length=200, null = True, choices = helpType)

    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)


# Create your models here.
# class AllLogout(models.Model):
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
#     logOutTime = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return str(self.user) + ': ' + str(self.logOutTime)