from django import template

register = template.Library()

@register.filter
def hashtag_link(post):
    content = post.content # #아침 #점심 #저녁 => <a>#고양이</a>
    hashtags = post.hashtags.all() # QuerySer [HashTag Object(1)....]
    for hashtag in hashtags:
        content = content.replace(
            f"{hashtag.content}",
            f'<a href="/posts/hashtags/{hashtag.id}/">{hashtag.content}</a>')
    return content