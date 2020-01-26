
from django.urls import path

from . import views

app_name = 'planner' # change later to whatever this is gonna be

urlpatterns = [
    # ex: /planner/
    path('', views.index, name='index'),
    # ex: /planner/5/
    path('<int:goal_id>/', views.detail, name='detail'),
    # ex: /planner/5/results/
    path('<int:goal_id>/results/', views.results, name='results'),
    # ex: /planner/5/vote/
    path('<int:goal_id>/vote/', views.vote, name='vote'),

    #path('<int:goal_id>/vote/', views.vote, name='vote'),
]