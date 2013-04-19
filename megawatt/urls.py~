from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from hello_polls.models import MyPoll

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=MyPoll.objects.order_by('-pub_date')[:3],
            context_object_name='poll_list',
            template_name='hello_polls/index.html')),
                       
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=MyPoll,
            template_name='hello_polls/details.html')),
                       
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=MyPoll,
            template_name='hello_polls/results.html'),
        name='hello_poll_results'),
                       
    url(r'^(?P<poll_id>\d+)/vote/$', 'hello_polls.views.vote'),
)