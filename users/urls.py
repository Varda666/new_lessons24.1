from django.urls import path

from users.views import UserListView, UserRetrieveView, UserUpdateView, UserCreateView, UserDestroyView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('<int:pk>/', UserRetrieveView.as_view(), name='user_detail'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('delete/<int:pk>/', UserDestroyView.as_view(), name='user_delete'),
    ]