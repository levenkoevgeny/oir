from django import template

register = template.Library()


@register.filter(name='get_sub_dict')
def get_sub_dict(value, key):
    return value[str(key)] if str(key) in value else {}


@register.filter(name='get_value_form_dict')
def get_value_form_dict(value, key):
    return value[str(key)] if str(key) in value else 0