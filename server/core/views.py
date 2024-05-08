from django.http import HttpResponse
from rest_framework import viewsets

from .models import Question
from .serializers import QuestionSerializer

def ping(_):
    return HttpResponse("pong")

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer