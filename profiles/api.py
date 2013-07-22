from django.core.serializers import json 
from tastypie.exceptions import Unauthorized
from django.utils import simplejson 
from tastypie.serializers import Serializer 
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from django.conf.urls.defaults import *
from profiles.models import *
from django.contrib.auth.models import User
from friendship.models import *
from django.contrib.contenttypes.models import ContentType
from phileo.models import *
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication ,ApiKeyAuthentication
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from profiles.authorization import GuardianAuthorization
from django.core.files.base import ContentFile

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


    



class SignupResource(ModelResource):
    class Meta:
        allowed_methods = ['post']
        object_class = User
        include_resource_uri = False
        fields = ['username']
        resource_name='register'
        authorization = Authorization()
        authentication = Authentication()

    def obj_create(self, bundle,request=None, **kwargs):
         username, password = bundle.data['username'], bundle.data['password']
         try:
             bundle.obj = User.objects.create_user(username,'',password)
         except IntegrityError:
             raise BadRequest('That username already exist')
         return bundle

       

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        serializer = PrettyJSONSerializer()
        excludes = []
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        list_allowed_methods = ['post','get']
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        filtering = {
            'username': ALL,
        }

        include_resoure_uri = True
    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<username>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
        ]




class ForkResource(ModelResource):
#    projects = fields.ToManyField('profiles.api.ProjectResource','projects', full=True)
    
    
    class Meta:
        queryset = Project.objects.all()
        serializer = PrettyJSONSerializer()
        excludes = ['id']
        list_allowed_methods = ['post','put','get','delete']
        resource_name = 'forking'
        include_resoure_uri = True
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
    
    def dehydrate(self, bundle):
        pro_id = int(bundle.obj.id)
        username = bundle.request.user
        bundle.data["history"] = bundle.obj.history
        def clone(pro_id,username):

            cloned = Project.objects.get(pk = pro_id)
            creator = cloned.user
            requester = Profile.objects.get(user = username)
            if creator == requester:
                changes = "none , you are the owner"
            else:
                cloned.id = None
                cloned.user = Profile.objects.get(user = username)
                new_file = ContentFile(cloned.src.read())
                new_screen = ContentFile(cloned.screenshot.read())
                new_file.name = cloned.src.name
                new_screen.name = cloned.screenshot.name
                cloned.screenshot = new_screen
                cloned.src = new_file
                changes = "project %s  created by %s forked by %s " % (cloned.title , creator, cloned.user)
                cloned.history = changes
                cloned.save()
            return changes

        
        bundle.data["history"] = clone(pro_id,username)#bundle.obj.history

        return bundle
    



class LikeResource(ModelResource):
    class Meta:
        queryset = Like.objects.all()
        serializer = PrettyJSONSerializer()
        excludes = ['id','receiver_object_id']
        resource_name = 'liking'
        include_resoure_uri = True
        authentication = Authentication()
        authorization = Authorization()
    def dehydrate(self, bundle):
        
        likes = Like.objects.filter(receiver_content_type=ContentType.objects.get_for_model(Project) , receiver_object_id=bundle.obj.id).count ()
        bundle.data["Likes"] = likes
   
        return bundle 

class FollowingResource(ModelResource):
    follower = fields.ToOneField(to='profiles.api.ProfileResource',attribute='follower',related_name="profile")           
    followee = fields.ToOneField(to='profiles.api.ProfileResource',attribute='followee',related_name="profile")
    class Meta:
        allowed_methods = ['post','put','patch','delete','get']
        queryset = Follow.objects.all()
        serializer = PrettyJSONSerializer()
        resource_name = "relations"
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        include_resource_uri = False

    def dehydrate(self, bundle):
        bundle.data["user"] = bundle.obj.follower
        qs = Follow.objects.filter(followee=bundle.obj.follower).all()
        followers = [u.follower for u in qs] 
        qs2 = Follow.objects.filter(follower=bundle.obj.follower).all()
        following = [u.followee for u in qs2] 
        bundle.data["followers"] = followers
        bundle.data["following"] = following
        return bundle

class CommentResource(ModelResource):
    class Meta:
        queryset = Comment.objects.all()
        serializer = PrettyJSONSerializer()
        excludes = ['id' ,'resource_uri','entry']
        incldue_resource_uri = True
        authorization = Authorization()
        authentication = Authentication()

    def dehydrate(self, bundle):
        bundle.data["entry"] = bundle.obj.entry
        return bundle


class MultipartResource(object):
    def deserialize(self, request, data, format=None):
        if not format:
            format = request.META.get('CONTENT_TYPE', 'application/json')
        if format == 'application/x-www-form-urlencoded':
            return request.POST
        if format.startswith('multipart'):
            data = request.POST.copy()
            data.update(request.FILES)
            return data
        return super(MultipartResource, self).deserialize(request, data, format)

    def put_detail(self, request, **kwargs):
        if not hasattr(request, '_body'):
            request._body = ''

        return super(MultipartResource, self).put_detail(request, **kwargs)
    

class ProjectResource(MultipartResource, ModelResource):
    user = fields.ForeignKey('profiles.api.ProfileResource' ,'user')
    comment = fields.ToManyField('profiles.api.CommentResource','comment', full=True, null=True) 
    src = fields.FileField(attribute="src", blank=True, null=True)
    screenshot = fields.FileField(attribute="screenshot", blank=True, null=True)
    class Meta:
        queryset = Project.objects.all()
        serializer = PrettyJSONSerializer()
        resource_name = 'projects'
        excludes = []
        list_allowed_methods = ['post','get','delete','put']
        include_resource_uri = True
        authorization = Authorization()#UserAuthorization()
        authentication = ApiKeyAuthentication()

    def dehydrate(self, bundle):
        
        bundle.data["owner"] = bundle.obj.user
        bundle.data["history"] = bundle.obj.history
        likes = Like.objects.filter(receiver_content_type=ContentType.objects.get_for_model(Project) , receiver_object_id=bundle.obj.id).count ()
        bundle.data["Likes"] = likes
    
        return bundle 




class ProfileResource(ModelResource):
    projects = fields.ToManyField('profiles.api.ProjectResource','ussr', full=True, null=True)
    user = fields.ForeignKey(UserResource ,'user')
    
    class Meta:
        queryset = Profile.objects.all()
        serializer = PrettyJSONSerializer()
        resource_name = 'profile'
        excludes = ['gender','birth_date','website']
        include_resource_uri = True
        list_allowed_methods = ['post','delete','get','put']
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        
    
    def dehydrate(self, bundle):
        bundle.data["user"] = bundle.obj.user
        qs = Follow.objects.filter(followee=bundle.obj.user).all()
        followers = [u.follower for u in qs] 
        qs2 = Follow.objects.filter(follower=bundle.obj.user).all()
        following = [u.followee for u in qs2] 
        bundle.data["followers"] = followers
        bundle.data["following"] = following
        return bundle

