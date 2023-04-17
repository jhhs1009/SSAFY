from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_list, name='articles'),
    path('articles/<int:article_pk>/', views.article_detail, name = "detail"),
    path('comments/', views.comment_list, name="comment_list")
    
]
