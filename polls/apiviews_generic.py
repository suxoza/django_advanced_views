from rest_framework import generics
from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer


#  Get a list of entities, or create them. Allows GET and POST
class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


# Retrieve an individual entity details, or delete the entity. Allows GET and DELETE
class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


#  Allows creating entities, but not listing them. Allows POST.
class CreateVote(generics.CreateAPIView):
    serializer_class = VoteSerializer
