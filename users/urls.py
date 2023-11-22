from django.urls import path

from users.views import (UserListView, UserRetrieveView, UserUpdateView, UserCreateView, UserDestroyView,
                         MyTokenObtainPairView, UserSubscriptionUpdatesCreateView, UserSubscriptionUpdatesDestroyView)

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('<int:pk>/', UserRetrieveView.as_view(), name='user_detail'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('delete/<int:pk>/', UserDestroyView.as_view(), name='user_delete'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/', UserSubscriptionUpdatesCreateView.as_view(), name='subscription_create'),
    path('token/', UserSubscriptionUpdatesDestroyView.as_view(), name='subscription_delete'),
    ]