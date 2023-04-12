from django import template

register = template.Library()

# artile안의 content를 검사해서
@register.filter
def hashtag_link(article):
    content = article.content
    hashtags = article.hashtags.all()

    # 해시태그들 링크로 만들어주기
    for hashtag in hashtags:
        content = content.replace(hashtag.content,
        f"<a href='/articles/{hashtag.pk}/hashtag/'>{hashtag.content}</a>")
    return content
    
    