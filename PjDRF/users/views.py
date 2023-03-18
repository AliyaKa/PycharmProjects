from rest_framework import mixins
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet

# from rest_framework.views import GenericViewSet

from .models import CustomUser as User
from .serializers import UserModelSerializer, UserSerializerWithFullName


class CustomUserViewSet(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        GenericViewSet):

    # class UserListApiView(ListAPIView):
    #
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserSerializerWithFullName
        return UserModelSerializer
