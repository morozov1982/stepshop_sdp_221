from django import template

register = template.Library()


@register.filter(name='my_split')
def my_split(string):
    if ':' in string:
        return string.split(':')[0]
    return string
