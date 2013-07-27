from django.db import models
from django.utils.translation import ugettext_lazy as _
from userena.models import UserenaLanguageBaseProfile,UserenaBaseProfile
from userena.utils import user_model_label
from django.contrib.auth.models import User
from tastypie.models import create_api_key
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
import datetime


models.signals.post_save.connect(create_api_key, sender=User)


class Profile(UserenaLanguageBaseProfile):
    """ Default profile """
    GENDER_CHOICES = (
        (1,_('Male')),
        (2, _('Female')),
    )

    user = models.OneToOneField(user_model_label,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile')

    gender = models.PositiveSmallIntegerField(_('gender'),
                                              choices=GENDER_CHOICES,
                                              blank=True,
                                              null=True)
    website = models.URLField(_('website'), blank=True)
    #photo = models.ImageField(upload_to='profiles')
    location =  models.CharField(_('location'), max_length=255, blank=True)
    birth_date = models.DateField(_('birth date'), blank=True, null=True)
    about_me = models.TextField(_('about me'), blank=True)
    def __unicode__(self):
        return self.user.username


    @property
    def age(self):
        if not self.birth_date: return False
        else:
            today = datetime.date.today()
            # Raised when birth date is February 29 and the current year is not a
            # leap year.
            try:
                birthday = self.birth_date.replace(year=today.year)
            except ValueError:
                day = today.day - 1 if today.day != 1 else today.day + 2
                birthday = self.birth_date.replace(year=today.year, day=day)
                if birthday > today: return today.year - self.birth_date.year - 1
            else: return today.year - self.birth_date.year
    def followers_count(self):
        return self.user.who_is_followed.all().count()



class Project(models.Model):
      user = models.ForeignKey(Profile, related_name='ussr')
      shared_date = models.DateTimeField('date published', blank=True)
      title = models.CharField(max_length=100) 
      desc =models.CharField(max_length=200, blank=True) 
      history = models.CharField(max_length=200,blank=True) 
      src = models.FileField(upload_to='projects' , blank=True , null=True) 
      screenshot = models.ImageField(upload_to='projects', blank=True,null=True)
    
      def save(self, *args, **kwargs):
          self.shared_date = timezone.now()
          super(Project, self).save(*args, **kwargs)
          
      def __unicode__(self):
          return self.title


class Comment(models.Model):
      user = models.ForeignKey(Profile, related_name='commenter')
      entry = models.ForeignKey(Project,related_name='comment')
      text = models.CharField(max_length=500)
    
      def __unicode__(self):
          return self.text


        
class Like(models.Model):
    
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile , related_name="likes")
    liked_content_type = models.ForeignKey(Project)
    shared_date = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = (
            ("user","liked_content_type"),
            )

    def __unicode__(self):
        return u"%s likes %s" % (self.user , self.liked_content_type)
