from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .userSerializers import UserSerializer
from django.contrib.auth import authenticate
from .serializers import PollSerializer, ChoiceSerializer
from .models import Poll, Choice
from rest_framework.exceptions import PermissionDenied
from rest_framework import viewsets


#  Allows creating entities, but not listing them. Allows POST.
class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            error = {"error": "Wrong Credentials"}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def destroy(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=self.kwargs["pk"])
        if not request.user == poll.created_by:
            raise PermissionDenied("You can not delete this poll.")
        return super().destroy(request, *args, **kwargs)


class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Choice.objects.filter(poll_id=self.kwargs["pk"])

    def post(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=self.kwargs["pk"])
        if not request.user == poll.created_by:
            raise PermissionDenied("You can not create choice for this poll.")
        return super().post(request, *args, **kwargs)

    serializer_class = ChoiceSerializer
