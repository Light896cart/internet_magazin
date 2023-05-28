from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView
from cart.forms import CartAddProductForm
from home.models import PictureHome
from main.models import Product
from main.utils import *

class HomeHome(ListView,DataMixin):
    model = Product
    template_name = 'home/home.html'
    context_object_name = 'posts'
    allow_empty = False

    # def get_queryset(self):
    #     return Product.objects.filter(collecproduct__slug=self.kwargs['collections_slug'])
    #     # queryset = self.model.objects.filter(collecproduct=self.category)
    #     # return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['picture'] = PictureHome.objects.all()
        context['posts'] = Collections.objects.all()
        context['product'] = Product.objects.all()
        context['catr'] = Category.objects.all()
        context['cart_product_form'] = CartAddProductForm
        return context


class MainCategory(DataMixin,ListView):
    model = Product
    template_name = 'home/collections.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):#если у is_published стоит галочка то мы публикуем запись если нет,то нет
        return Product.objects.filter(collecproduct__slug=self.kwargs['collections_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.all()
        c_def = self.get_user_context(title='Категория - '+ str(context['product'][0].collecproduct),
                                      cat_selected=context['product'][0].collecproduct)
        return dict(list(context.items()) + list(c_def.items()))


