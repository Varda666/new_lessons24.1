from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from users.models import User, UserSubscriptionUpdates
from lms_service.permissions import IsOwnerOrNot, IsOwner
from users.serializers import UserSerializer, UserSubscriptionUpdatesSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserSubscriptionUpdatesCreateView(CreateAPIView):
    queryset = UserSubscriptionUpdates.objects.all()
    serializer_class = UserSubscriptionUpdatesSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all(), UserSubscriptionUpdates.objects.all()
    serializer_class = UserSerializer, UserSubscriptionUpdatesSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrNot]

class UserDestroyView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser | IsOwner]


class UserSubscriptionUpdatesDestroyView(DestroyAPIView):
    queryset = UserSubscriptionUpdates.objects.all()
    serializer_class = UserSubscriptionUpdatesSerializer
    permission_classes = [IsAdminUser | IsOwner]


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
