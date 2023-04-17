from .models import Article
from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title',)
        
class ArticleListSerializer(serializers.ModelSerializer):
    article_set = ArticleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = "__all__"