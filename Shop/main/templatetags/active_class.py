from django import template

register = template.Library()

@register.filter
def active_class(a, b):
    if a == b:
         return 'active'
    else:
        return 'inactive'

