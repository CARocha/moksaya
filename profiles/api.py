from django.core.serializers import json 
from django.utils import simplejson 
from tastypie.serializers import Serializer 
from tastypie.resources import ModelResource 
from tastypie import fields
from django.conf.urls.defaults import *
from profiles.models import *
from django.contrib.auth.models import User
from friendship.models import *
from django.contrib.contenttypes.models import ContentType
from phileo.models import *
from tastypie.authorization import Authorization


class PrettyJSONSerializer(Serializer): 
    json_indent = 4 
 
    def to_json(self, data, options=None): 
        options = options or {} 
        data = self.to_simple(data, options) 
        return simplejson.dumps(data, cls=json.DjangoJSONEncoder, sort_keys=True, ensure_ascii=False, indent=self.json_indent) 
    def from_json(self, content):
        data = simplejson.loads(content)

        if 'requested_time' in data:
            # Log the request here...
            pass

        return data

class ForkResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        serializer = PrettyJSONSerializer()
        excludes = ['id']
        list_allowed_methods = ['post']
        resource_name = 'forking'
        include_resoure_uri = True
    
    def dehydrate(self, bundle):
        pro_id = int(bundle.obj.id)
        username = bundle.request.user
        bundle.data["history"] = bundle.obj.history
        def clone(pro_id,username):

            cloned = Project.objects.get(pk = pro_id)
            creator = cloned.owner
            requester = Profile.objects.get(user = username)
            if creator == requester:
                changes = "none , you are the owner"
            else:
                forked = cloned.fork()
                forked.owner = Profile.objects.get(user = username)
                changes = forked.diff(cloned)
                #forked.history= changes)
                #bundle.data["history"] = (changes)
                #bundle.data["Owner"] = bundle.obj.owner
                
                #forked.history = changes # bundle.data["history"]
                forked.commit()
                
            return changes

        bundle.obj.history =  clone(pro_id,username)
        bundle.data["history"] = bundle.obj.history

        return bundle
    

    
  #  def dehydrate(self, bundle):
  #      bundle.data["Owner"] = bundle.obj.owner
  #      bundle.data["history"] = bundle.obj.history

         
        
   #     return bundle 




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
        excludes = []
        #list_allowed_methods = ['post','get','delete']
        include_resource_uri = False

    def dehydrate(self, bundle):
        
        bundle.data["owner"] = bundle.obj.owner
        bundle.data["history"] = bundle.obj.history
        likes = Like.objects.filter(receiver_content_type=ContentType.objects.get_for_model(Project) , receiver_object_id=bundle.obj.id).count ()
        bundle.data["Likes"] = likes
    
        return bundle 



class ProfileResource(ModelResource):
    projects = fields.ToManyField('profiles.api.ProjectResource','projects', full=True)
    
    class Meta:
        queryset = Profile.objects.all()
        serializer = PrettyJSONSerializer()
        resource_name = 'profile'
        excludes = ['id','gender','birth_date']
        include_resource_uri = False
       # authorization = Authorization()
    
    def dehydrate(self, bundle):
        bundle.data["user"] = bundle.obj.user
        all_friends = Friend.objects.friends(bundle.obj.user)
        bundle.data["friends"] = all_friends
        return bundle
