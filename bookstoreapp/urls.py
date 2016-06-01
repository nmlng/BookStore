from django.conf.urls import url

from . import views

app_name = 'bookstoreapp'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='indexamos'),
    url(r'^createbook$', views.bookcreate, name='bookcreate'),
    url(r'^createeditor$', views.editorcreate, name='editorcreate'),
    url(r'^createauthor$', views.authorcreate, name='authorcreate'),
    url(r'^createcategory$', views.categorycreate, name='authorcreate'),
    url(r'^(?P<category_id>[0-9]+)/books/$', views.category_view, name='category_view'),
#    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
