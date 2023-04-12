from django import template

register = template.Library()

# artile안의 content를 검사해서
@register.filter
def hashtag_link(movie):
    content = movie.content
    hashtags = movie.hashtags.all()

    # 해시태그들 링크로 만들어주기
    for hashtag in hashtags:
        content = content.replace(hashtag.content,
        f"<a href='/movies/{hashtag.pk}/hashtag/'>{hashtag.content}</a>")
    return content
    
    