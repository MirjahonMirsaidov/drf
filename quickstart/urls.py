from django.urls import include, path
from quickstart import views


urlpatterns = [
    path('users/', views.UserListCreateView.as_view()),
    path('users/<int:pk>', views.UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
]