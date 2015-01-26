from django import template
from news.models import News

register = template.Library()

@register.inclusion_tag('left_news.html')
def leftnews():
    return {'news': News.objects.all().order_by('-news_date')[:10]}