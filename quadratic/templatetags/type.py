from django import template

register = template.Library()


@register.filter(name='get_type')
def get_type(value):
    return isinstance(value, int)
