from django import template
from atexit import register

register=template.Library()

@register.filter(name='get_val')

def get_val(dict,key):
    return dict.get(key)