from django.core.serializers import json 
from django.utils import simplejson 
from tastypie.serializers import Serializer 
from tastypie.resources import ModelResource 
from tastypie import fields
from django.db.models import Q
from profiles.models import *
from django.contrib.auth.models import User
from friendship.models import *
from django.contrib.contenttypes.models import ContentType
from phileo.models import *

class PrettyJSONSerializer(Serializer): 
    json_indent = 4 
 
    def to_json(self, data, options=None): 
        options = options or {} 
        data = self.to_simple(data, options) 
        return simplejson.dumps(data, cls=json.DjangoJSONEncoder, sort_keys=True, ensure_ascii=False, indent=self.json_indent) 
 

class ForkResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        serializer = PrettyJSONSerializer()
        excludes = ['id']
        resource_name = 'forking'
        include_resoure_uri = True
       
    def dehydrate(self, bundle):
        pro_id = int(bundle.obj.id)
        username = bundle.request.user
# following method clones the requested project to current users profile
#For now this works as get /forking/pk/        
        def clone(pro_id,username):

            cloned = Project.objects.get(pk = pro_id)
            creater = cloned.owner
            requester = Profile.objects.get(user = username)
            if creater == requester:
                changes = "none , you are the owner"
            else:
                forked = cloned.fork()
                forked.owner = Profile.objects.get(user = username)
                forked.commit()
                changes = forked.diff(cloned)
            
            return changes


        bundle.data["Changes"]= clone(pro_id,username) 

        return bundle 


class LikeResource(ModelResource):
    class Meta:
        queryset = Like.objects.all()
        serializer = PrettyJSONSerializer()
        excludes = ['id','receiver_object_id']
        resource_name = 'liking'
        include_resoure_uri = True

    def dehydrate(self, bundle):
        
        likes = Like.objects.filter(receiver_content_type=ContentType.objects.get_for_model(Project) , receiver_object_id=bundle.obj.id).count ()
        bundle.data["Likes"] = likes
   
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
        likes = Like.objects.filter(receiver_content_type=ContentType.objects.get_for_model(Project) , receiver_object_id=bundle.obj.id).count ()
        bundle.data["Likes"] = likes
    
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
        bundle.data["user"] = bundle.obj.user
        all_friends = Friend.objects.friends(bundle.obj.user)
        bundle.data["friends"] = all_friends
        return bundle
