from tastypie.resources import ModelResource 
from tastypie import fields
from profiles.models import *
from django.contrib.auth.models import User


class CommentResource(ModelResource):
    class Meta:
        queryset = Comment.objects.all()
        excludes = ['id' , 'resource_uri','entry']
        incldue_resource_uri = True
#    def dehydrate(self, bundle):
#        bundle.data["entry"] = bundle.obj.entry
#        return bundle



class ProjectResource(ModelResource):
    
    comment = fields.ToManyField('profiles.api.CommentResource','comment', full=True) 

    class Meta:
        queryset = Project.objects.all()
        resource_name = 'projects'
        excludes = ['id']
        include_resource_uri = False

    def dehydrate(self, bundle):
        bundle.data["owner"] = bundle.obj.owner
        return bundle 



class ProfileResource(ModelResource):
    
    projects = fields.ToManyField('profiles.api.ProjectResource','projects', full=True)
    
    class Meta:
        queryset = Profile.objects.all()
        resource_name = 'profile/list'
        excludes = ['id']
        include_resource_uri = False
    
    def dehydrate(self, bundle):
        bundle.data["user"] = bundle.obj.user
        return bundle 
