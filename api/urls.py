from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateView, DetailsView, UserView, UserDetailsView, HomePageView, GetInputData


urlpatterns = {
	# path('bucketlists/', CreateView.as_view(), name="create"),
	# path('bucketlists/<int:pk>/', DetailsView.as_view(), name="details"),
	path('get_data/', GetInputData.as_view(), name='get_data'),
	path('auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('users/', UserView.as_view(), name="users"),
	path('users/<int:pk>/', UserDetailsView.as_view(), name="user_details"),
	path('get-token/', obtain_auth_token),
	path('', HomePageView.as_view(), name='index'),

}

urlpatterns = format_suffix_patterns(urlpatterns)
