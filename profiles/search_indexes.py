#import datetime
from haystack import indexes 
from profiles.models import *

class ProjectIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    titled = indexes.CharField(model_attr="title")
    info = indexes.CharField(model_attr="desc")
    commits = indexes.CharField(model_attr="history")
    #pub_date = indexes.DateTimeField(model_attr="shared_date")


    def get_model(self):
        return Project

    def index_queryset(self, using=None):
        return self.get_model().objects

