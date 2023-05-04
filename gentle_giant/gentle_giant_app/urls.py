from django.urls import path
from gentle_giant_app import views

urlpatterns=[
    path('', views.index, name='index'),
    path('howto/', views.howto, name='howto')
]