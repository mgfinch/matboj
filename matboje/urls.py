from django.conf.urls import url

from matboje import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.MatbojDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.MatbojResults.as_view(), name='results'),
    url(r'^(?P<pk>\d+)/submitpage/$', views.MatbojSubmitPage.as_view(), name='submit_page'),
    url(r'^(?P<pk>\d+)/SubmitMatch/$', views.SubmitMatch, name='submit_match'),
    url(r'^(?P<pk>\d+)/submitpage/SubmitMatch/$', views.SubmitMatch, name='submit_match'),
    url(r'^(?P<pk>\d+)/MatbojAdmin/$', views.MatbojAdminView.as_view(), name='matboj_admin'),
]
