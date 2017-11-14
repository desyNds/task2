from django.conf.urls import url
from member import views

urlpatterns = [
    url(r'^try$', views.TryView.as_view(), name='try'),
    url(r'^try1$', views.TryView1.as_view(), name='try1'),
    url(r'^try2$', views.TryView2.as_view(), name='try2'),
    url(r'^tpl$', views.TryTplView.as_view(), name='tpl'),
]