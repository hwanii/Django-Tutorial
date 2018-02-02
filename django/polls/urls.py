from django.urls import path, re_path
from . import views

urlpatterns = [
    path('polls/', views.index, name='index'),
    path('polls/<int:question_id>/', views.detail, name='detail'),
    path('polls/<int:question_id>/results/', views.results, name='results'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),

    re_path(r'polls/^(?P<question_id>\d+)/$', views.detail, name='detail'),
    re_path(r'polls/^(?P<question_id>\d+)/results/$', views.results, name='results'),
    re_path(r'polls/^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
]