from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleListSerializer

# 여기 아래
from rest_framework import status


@api_view(["GET","POST"])
def article_list(request):
    if request.method == "GET":
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article =get_object_or_404(Article, pk=article_pk)
    if request.method == "GET":
        serializer = ArticleListSerializer(article)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ArticleListSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == "DELETE":
        article.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)