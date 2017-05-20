from rest_framework import serializers
from .models import Article

from users.serializer import UserSerializer

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Article
        fields = ('id', 'user','title', 'content', 'image')