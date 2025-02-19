from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить книгу", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
]

class DataMixin:
    paginate_by = 2


    def get_user_context(self, **kwargs):
        context = kwargs
        categors = Category.objects.all()
        context['menu'] = menu
        context['categors'] = categors
        if 'categor_selected' not in context:
            context['categor_selected'] = 0
        return context
