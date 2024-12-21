from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def display_queen_color(value):
    if value == "white":
        return "bg-white-500"
    elif value == "yellow":
        return "bg-yellow-500"
    elif value == "red":
        return "bg-red-500"
    elif value == "green":
        return "bg-green-500"
    elif value == "blue":
        return "bg-blue-500"
    else:
        return "bg-gray-500"

@register.filter
def display_boolean_icon(value):
    if value:
        return mark_safe('<i class="fa fa-check" style="color:green"></i>')
    else:
        return mark_safe('<i class="fa fa-times" style="color:red"></i>')
