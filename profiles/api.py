from django.core.serializers import json 
from django.utils import simplejson 
from tastypie.serializers import Serializer 
from tastypie.resources import ModelResource 
from tastypie import fields
from django.db.models import Q
from profiles.models import *
from django.contrib.auth.models import User
from friendship.models import *
from phileo.models import *

class PrettyJSONSerializer(Serializer): 
    json_indent = 4 
 
    def to_json(self, data, options=None): 
        options = options or {} 
        data = self.to_simple(data, options) 
        return simplejson.dumps(data, cls=json.DjangoJSONEncoder, sort_keys=True, ensure_ascii=False, indent=self.json_indent) 
 


class FriendResource(ModelResource):
    class Meta:
        queryset = Friend.objects.all()
        serializer = PrettyJSONSerializer()
        excludes = ['id']
        resource_name= 'friends'
        include_resource_uri = True
    def dehydrate(self, bundle):
        all_friends = Friend.objects.friends(bundle.request.user)
        return all_friends
 
class LikeResource(ModelResource):
    class Meta:
        queryset = Like.objects.all()
        serializer = PrettyJSONSerializer()
        excludes = ['id']
        resource_name = 'liking'
        include_resoure_uri = True
    def dehyrdate(self, bundle):
        bundle.data["sender"]= bundle.obj.sender
        return bundle
    
     

class CommentResource(ModelResource):
    class Meta:
        queryset = Comment.objects.all()
        serializer = PrettyJSONSerializer()
        excludes = ['id' ,'resource_uri','entry']
        incldue_resource_uri = True
    def dehydrate(self, bundle):
        bundle.data["entry"] = bundle.obj.entry
        return bundle



class ProjectResource(ModelResource):

    comment = fields.ToManyField('profiles.api.CommentResource','comment', full=True) 

    class Meta:
        queryset = Project.objects.all()
        serializer = PrettyJSONSerializer()
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
        serializer = PrettyJSONSerializer()
        resource_name = 'profile/list'
        excludes = ['id']
        include_resource_uri = False
    
    def dehydrate(self, bundle):
        all_friends = Friend.objects.friends(bundle.obj.user)
        bundle.data["user"] = bundle.obj.user
        return bundle, all_friends 
