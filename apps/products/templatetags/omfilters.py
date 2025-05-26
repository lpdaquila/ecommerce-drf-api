from django.template import Library
from utils import template_filters

register = Library()

@register.filter
def format_price(value):
    return template_filters.format_price(value)