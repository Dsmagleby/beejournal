from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def display_queen_color(value):
    if value in ["white", "yellow", "red", "green", "blue"]:
        return f"bg-{value}-500"
    else:
        return "bg-gray-500"

@register.filter
def display_boolean_icon(value):
    if value:
        return mark_safe('<i class="fa fa-check" style="color:green"></i>')
    else:
        return mark_safe('<i class="fa fa-times" style="color:red"></i>')
