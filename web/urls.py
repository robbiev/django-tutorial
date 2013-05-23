from django.conf.urls import patterns, url

from web import views

urlpatterns = patterns('',
  url(r'^$', views.IndexView.as_view(), name='index'),
  url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
  url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
  url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
#  url(r'^$', views.index, name='index'),
#
#  # /poll/5
#  url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
#  # /polls/5/results/
#  url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
#  # /polls/5/vote/
#  url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
