from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import AV, Device_Types
from .serializers import AVSerializer, UserSerializer
#from .permissions import IsOwnerOrReadOnly



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'av': reverse('av-list', request=request, format=format)
    })



class UserList(generics.ListAPIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserDetail(generics.RetrieveAPIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = UserSerializer



class av_list(generics.ListCreateAPIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = AV.objects.all()
    serializer_class = AVSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)



class av_detail(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = AV.objects.all()
    serializer_class = AVSerializer