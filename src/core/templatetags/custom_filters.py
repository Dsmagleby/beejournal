from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def queen_color_badge(value, color_name):
    if value in ["white", "yellow", "red", "green", "blue"]:
        return mark_safe(f'<div class="badge bg-{value}-500">{color_name}</div>')
    else:
        return mark_safe(f'<div class="badge bg-gray-500">{color_name}</div>')


@register.filter
def display_boolean_icon(value):
    if value:
        return mark_safe('<i class="fa fa-check" style="color:green"></i>')
    else:
        return mark_safe('<i class="fa fa-times" style="color:red"></i>')
