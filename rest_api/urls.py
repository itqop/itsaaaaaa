from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, UserView, UserDetailsView, HomePageView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
    url(r'^auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
    url(r'^users/$', UserView.as_view(), name="users"),
    url(r'^users/(?P<pk>[0-9]+)/$',
        UserDetailsView.as_view(), name="user_details"),
    url(r'^get-token/', obtain_auth_token),
    # url(r'^', HomePageView.as_view(), name='index'),

}

urlpatterns = format_suffix_patterns(urlpatterns)
