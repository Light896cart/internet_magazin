from .models import *
from cart.forms import CartAddProductForm


class DataMixin:
    def get_user_context(self,**kwargs):#создает контекст для шаблона(убирает дублирование кода)
        context = kwargs#создаем первоначальный список
        cats = Category.objects.all()
        catr = Category.objects.all()
        catl = Subcategory.objects.all()
        collec = Collections.objects.all()
        cart_product_form = CartAddProductForm
        context['cart_product_form'] = cart_product_form
        context['catl'] = catl
        context['cats'] = cats
        context['collec'] = collec
        context['catr'] = catr

        # context['size'] = size
        return context