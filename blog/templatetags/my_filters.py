from django.template import Library
register = Library()
@register.filter(name='times') 
def times(start, end):
    return range(start, end)