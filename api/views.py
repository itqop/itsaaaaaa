import json

from django.contrib.auth.models import User
from django.views.generic.base import TemplateView

from rest_framework import generics, permissions
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response

from api.services.model import get_n_best
from .permissions import IsOwner
from .serializers import BucketlistSerializer, UserSerializer
from .models import Bucketlist


class CreateView(generics.ListCreateAPIView):
	"""This class handles the GET and POSt requests of our rest api."""
	queryset = Bucketlist.objects.all()
	serializer_class = BucketlistSerializer
	permission_classes = (
		permissions.IsAuthenticated,
		IsOwner)

	def perform_create(self, serializer):
		"""Save the post data when creating a new bucketlist."""
		serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""This class handles GET, PUT, PATCH and DELETE requests."""

	queryset = Bucketlist.objects.all()
	serializer_class = BucketlistSerializer
	permission_classes = (
		permissions.IsAuthenticated,
		IsOwner)


class UserView(generics.ListAPIView):
	"""View to list the user queryset."""
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
	"""View to retrieve a user instance."""
	queryset = User.objects.all()
	serializer_class = UserSerializer


class HomePageView(TemplateView):
	template_name = 'index.html'


class GetInputData(APIView):
	"""
	Сбор входных данных 
	На вход получает один параметр
	Возвращает строчку

	пример: http://127.0.0.1:8000/get_data/?sphere=clinic&numbest=5
	"""
	@staticmethod
	def get(request):
		
		try:
			# Входные аргументы
			arg_sphere = str(request.query_params.get('sphere'))
			arg_numbest = int(request.query_params.get('numbest'))
			data = get_n_best(arg_sphere, arg_numbest)

			# Пребразовать массив в строку
			result = json.dumps(data, ensure_ascii=False,)
		
		except Exception as e:
			return Response(data={
				'Error': str(e),
				'message': 'Ошибка!'
			}, status=HTTP_400_BAD_REQUEST) #HTTP_400_BAD_REQUEST

		return Response(data={
			'result': result,
		}, status=HTTP_200_OK)