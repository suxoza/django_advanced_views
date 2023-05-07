from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Choice
from .serializers import ChoiceSerializer, VoteSerializer


class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Choice.objects.filter(poll_id=self.kwargs["pk"])

    serializer_class = ChoiceSerializer


class CreateVote(APIView):
    serializer_class = VoteSerializer

    def post(self, request, pk, choice_pk):
        data = {
            "choice": choice_pk,
            "poll": pk,
            "voted_by": request.data.get("voted_by"),
        }
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            print(vote)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
