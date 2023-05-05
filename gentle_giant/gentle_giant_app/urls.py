from django.urls import path
from gentle_giant_app import views

urlpatterns=[
    path('', views.index, name='index'),
    path('howto/', views.howto, name='howto'),
    path('', views.tables_view, name='gentle_giant_app'),
    path('home/', views.home, name='table'),
    path('game/', views.game, name='game'),
]