from django.http import HttpResponse
from rest_framework import viewsets

from .models import Question
from .serializers import QuestionSerializer

def ping(request):
    return HttpResponse("pong")

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()