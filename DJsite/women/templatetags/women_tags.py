from django import template
from women.models import *


register = template.Library() # register self-templaetetags
# simple tags return data collection
# inclusion tags return snippet of html page

@register.simple_tag(name="getcats") # The function becomes a simple tag
def get_categories(filter=None): # function for tag
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0): # returns html page
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}


