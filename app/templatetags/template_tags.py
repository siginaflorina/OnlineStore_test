from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def split(s, sep):
    return s.split(sep)


@register.filter
def range_to_n(n):
    return range(0, n)


@register.filter
def range_to_5_minus_n(n):
    return range(0, 5 - n)
