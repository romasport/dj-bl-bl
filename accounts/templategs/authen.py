from django import template

register = template.Library()

@register.inclusion_tag('login.html')
def login():
    return 0
