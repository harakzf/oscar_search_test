from django.urls import path
from django.conf.urls import url
from . import views
#from .views import IndexView


# どのアプリのurlsなのか分かるようにapp_nameを使用する。
app_name = 'srhapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
