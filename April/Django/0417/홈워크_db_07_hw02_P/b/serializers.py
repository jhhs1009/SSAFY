# b- serializers.py


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializers(
        many=True,
        read_only = True,
    )

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', '__(b)__')