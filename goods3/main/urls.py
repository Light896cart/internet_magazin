from django.urls import path#формирует маршруты
from django.views.decorators.cache import cache_page
from .views import *



urlpatterns = [
    path('',(GoodsHome.as_view()),name='main'),
    path('search/',Search.as_view(),name='search'),
    path('about/',about,name='about'),
    path('personal_data/',personal_data,name='personal_data'),
    path('post/<slug:post_slug>/',ShowPost.as_view(),name='post'),
    path('sort/<str:sort_type>', SortItems.as_view(), name='sort'),
    path('delivery/',Delivery.as_view(),name='delivery'),
    path('category/<slug:cat_slug>/',MainCategory.as_view(),name='category'),
    path('categort/<slug:catsub_slug>/',MainSubcategory.as_view(),name='subcategory'),
]