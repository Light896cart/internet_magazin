from main.models import Collections, Product
from .models import *
from cart.forms import CartAddProductForm


class DataMixin:
    def get_user_context(self,**kwargs):#создает контекст для шаблона(убирает дублирование кода)
        context = kwargs#создаем первоначальный список
        picture = PictureHome.objects.all()
        posts = Collections.objects.all()
        product = Product.objects.all()
        context['picture'] = picture
        context['posts'] = posts
        context['posts'] = product
        return context