from django.urls import path

from . import views

app_name = 'translate'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('translate', views.translate, name='translate'),
    path('analysis', views.analysis, name='analysis'),
    path('video', views.video, name='video'),
    path('ajax/getVal', views.testApi, name='getval'),
]
