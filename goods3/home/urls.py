from django.urls import path#формирует маршруты
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('',HomeHome.as_view(),name='home'),
    path('collections/<slug:collections_slug>/',MainCategory.as_view(),name='collections')
]