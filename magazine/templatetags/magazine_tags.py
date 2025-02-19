from django import template
from magazine.models import *

register = template.Library()

@register.simple_tag(name='getcategories')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('magazine/list_categories.html')
def show_categories(sort=None, categor_selected=0):
    if not sort:
        categors = Category.objects.all()
    else:
        categors = Category.objects.order_by(sort)

    return {"categors": categors, "categor_selected": categor_selected}
