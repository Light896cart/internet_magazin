
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q, Count
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import generic, View
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from taggit.models import Tag

from cart.forms import CartAddProductForm
from main.models import *
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .serializers import ProductSerializer
from .utils import *

posts = Product.objects.all()
subcat = Subcategory.objects.all()
catr = Category.objects.all()

class GoodsHome(generics.ListCreateAPIView):#показывает
    queryset = Product.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = ProductSerializer
    template_name = 'main/index.html'

    def get(self, request, pk=None):
        profile = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer
        queryset = Product.objects.all()
        return Response({'profiles': queryset})
    def get_queryset(self):
        return Product.objects.filter(is_published=True)

class WomenAPIUpdate(generics.RetrieveUpdateDestroyAPIView):#меняет
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class WomenAPIDestroy(generics.RetrieveDestroyAPIView):#удаляет
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class GoodsHome(DataMixin,ListView):
#     model = Product
#     template_name = 'main/index.html'
#     context_object_name = 'posts'
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Главная страница')
#         return dict(list(context.items())+list(c_def.items()))
#     def get_queryset(self):#если у is_published стоит галочка то мы публикуем запись если нет,то нет
#         return Product.objects.filter(is_published = True)


class SortItems(GoodsHome):#сортировка товара
    def get_queryset(self,*args,**kwargs):
        sort_types = {
            '0': '-time_create',
            '1': 'time_create',
            '2': 'price',
            '3': '-price',
        }

        sort_type = sort_types[self.kwargs['sort_type']]

        if 'query' in self.kwargs:
            query = self.kwargs['query']
            return super(SortItems, self).get_queryset().filter(Q(artist__icontains=query) |
                                                                Q(album__icontains=query)).order_by(sort_type)

        return super(SortItems, self).get_queryset().order_by(sort_type)




# class about(ListView,DataMixin):
#     model = Product
#     template_name = 'main/about.html'
#     context_object_name = 'post'
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         cart_product_form = CartAddProductForm()
#         c_def = self.get_user_context(title='Главная страница')
#         return dict(list(context.items()) + list(c_def.items()))
def about(request):
     return render(request, 'main/about.html')

def personal_data(request):
     return render(request, 'main/personal_data.html')


class Delivery(ListView,DataMixin):
    model = Product
    template_name = 'main/delivery.html'
    context_object_name = 'post'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))



class ShowPost(DataMixin,DetailView):
    model = Product
    template_name = 'main/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    form_class = CartAddProductForm


    def get_context_data(self,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        similar_posts = self.object.tags.similar_objects()[:2:-1]
        c_def = self.get_user_context(title=context['post'])
        context.update({
            'similar_posts':similar_posts
        })
        return dict(list(context.items())+list(c_def.items()))




class MainCategory(DataMixin,ListView):
    model = Product
    template_name = 'main/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):#если у is_published стоит галочка то мы публикуем запись если нет,то нет
        return Product.objects.filter(prod_sub_category__slug=self.kwargs['cat_slug'],is_published = True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - '+ str(context['posts'][0].prod_sub_category),
                                      cat_selected=context['posts'][0].prod_sub_category)
        return dict(list(context.items())+list(c_def.items()))

class MainSubcategory(DataMixin,ListView):
    model = Product
    template_name = 'main/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):#если у is_published стоит галочка то мы публикуем запись если нет,то нет
        return Product.objects.filter(subproduct__slug=self.kwargs['catsub_slug'],is_published = True).select_related('prod_sub_category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Подкатегория - '+ str(context['posts'][0].subproduct),
                                      cat_selected=context['posts'][0].subproduct)
        return dict(list(context.items()) + list(c_def.items()))

class Search(DataMixin,ListView):
    model = Product
    template_name = 'main/search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Product.objects.filter(title__iregex=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['q'] = self.request.GET.get('q')
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))