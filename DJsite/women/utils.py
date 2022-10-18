from .models import *
from django.db.models import Count

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        ]

class DataMixin:
        paginate_by = 2

        def get_user_context(self, **kwargs):
                context = kwargs # A dictionary of key and words that were passed to get_user_context function
                cats = Category.objects.annotate(Count('women'))
                user_menu = menu.copy() # to save our menu
                if not self.request.user.is_authenticated: # if user is not authenticated than we delete "Добавить сатью" from menu
                        user_menu.pop(1)
                context['menu'] = user_menu
                context['cats'] = cats
                if 'cat_selected' not in context:
                        context['cat_selected'] = 0
                return context