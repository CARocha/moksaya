from django.db import models
#from django.contrib.auth.models import User
import django.contrib.auth.models as auth
from account.models import *


class Projects(models.Model):
      owner = models.ForeignKey(auth.User)
      shared_date = models.DateTimeField('date published')
      title = models.CharField(max_length=100)
      desc = models.CharField(max_length=200)
      src = models.FileField(upload_to='proejcts')
      screenshot = models.ImageField(upload_to='projects')
    
      def save(self, *args, **kwargs):
          self.shared_date = timezone.now()
          super(Projects, self).save(*args, **kwargs)
      def __unicode__(self):
          return self.title

class Comment(models.Model):
      entry = models.ForeignKey(Projects)
      text = models.CharField(max_length=500)
    
      def __unicode__(self):
          return self.text

