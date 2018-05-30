from django.db import models
from django.contrib import auth
# Create your models here.


class User(auth.models.User, auth.models.PermissionsMixin):
    '''
    This will initialize the user class which inherits classes
    from the django.contrib class
    '''

    def __str__(self):
        '''
        This is a string reperesentation of each user
        '''
        return "@{}".format(self.username)
