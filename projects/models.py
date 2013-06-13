from django.db import models
from account.models import *

class ProjectOwner(models.Model):
    sugar_user = models.ForeignKey(Account.user)
    def __unicode__(self):
        return self.sugar_user

class Projects(models.Model):
    owner = models.ForeignKey(ProjectOwner)
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
"""
    def to_dict(self):
        entry = model_to_dict(self)
        entry.pop('screenshot')
        entry.pop('src')
        entry['shared_date'] = str(self.shared_date)
        return entry """


class Comment(models.Model):
    entry = models.ForeignKey(Projects)
    text = models.CharField(max_length=500)
    
    def __unicode__(self):
        return self.text

