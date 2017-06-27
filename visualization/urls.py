from django.conf.urls import url
from visualization import views

urlpatterns = [
    url(r'^$', views.MeterialList.as_view(), name='index'),
    url(r'^(?P<material_id>[0-9]+)/$', views.detail, name='detail'),
#    url(r'^$', views.index, name='index'),
]
