from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Poll


def polls_list(request):
    polls = Poll.objects.all()[:20]
    data = {
        "results": list(polls.values("question", "created_by__username", "created_at"))
    }
    return JsonResponse(data)


def polls_details(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {
        "results": {
            "question": poll.question,
            "created_by": poll.created_by.username,
            "created_at": poll.created_at,
        }
    }
    return JsonResponse(data)
