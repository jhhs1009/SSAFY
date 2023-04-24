from rest_framework import serializers
from .models import Actor,Movie,Review


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview',)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)

# 배우에 타이틀 뽑는거
class MovieActorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)

# 배우 디테일에 최종적으로 나오는거
class ActorDetailSerializer(serializers.ModelSerializer):
    movies = MovieActorDetailSerializer(many=True, read_only='True')
    
    class Meta:
        model = Actor
        fields = ('id','movies','name')


# 무비 디테일에 actors name만 나오게
class MovieActorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name',)
        
        
# 무비 디테일에 title content만 나오게
class MovieReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title','content',)
        
        
# 무비 디테일에 최종적으로 나오는거
class MovieDetailSerializer(serializers.ModelSerializer):
    actors = MovieActorDetailSerializer(many=True, read_only=True)
    review_set = MovieReviewDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = ('id','actors', 'review_set','title','overview','release_date','poster_path')


        
# 리뷰 디테일에 movie 뽑기
class ReviewMovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=  Movie
        fields = ('title',)

# 리뷰 디테일에 최종적으로 나오는거
class ReviewDetailSerializer(serializers.ModelSerializer):
    movie = ReviewMovieDetailSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('id','movie','title','content')
        
        
