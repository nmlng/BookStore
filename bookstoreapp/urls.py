from django.conf.urls import url

from . import views

app_name = 'bookstoreapp'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create$', 'bookstoreapp.views.bookcreate', name='bookcreate'),
    url(r'^(?P<category_id>[0-9]+)/books/$', views.categoryView, name='categoryView'),
#    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
