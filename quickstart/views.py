from django.contrib.auth.models import User
from django.core.cache import cache
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from quickstart.serializers import UserSerializer
from helper import timer


@method_decorator(cache_page(15*60, key_prefix='user-list'), name='list')
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
