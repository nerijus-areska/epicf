from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'main'
urlpatterns = [

    path('stats/', TemplateView.as_view(template_name='stats.html'), name='stats'),
    path('town/', TemplateView.as_view(template_name='town.html'), name='town'),
    path('test/', TemplateView.as_view(template_name='test.html'), name='test'),
    path('shop/', views.shop, name='shop'),
    path('items/', views.items, name='items'),
    path('areas/', TemplateView.as_view(template_name='areas.html'), name='areas'),
    path('area/', TemplateView.as_view(template_name='area.html'), name='area'),

    # ex: /main/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /main/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /main/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]