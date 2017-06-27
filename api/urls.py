from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^query/(?P<material_id>\d+)$', views.query, name='query'),
]
