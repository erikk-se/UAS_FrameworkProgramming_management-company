from django import template

register = template.Library()

@register.filter
def range_filter(value):
    """
    Custom filter to generate a range up to the given value.
    Usage: {% for i in n|range_filter %}
    """
    return range(int(value))
