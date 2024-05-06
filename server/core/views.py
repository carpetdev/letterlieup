from django.http import HttpResponse

from .models import Question

def ping(request):
    return HttpResponse("pong")

def index(request):
    latest_question_list = Question.objects.order_by('-date_added')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def list_answers(request):
    response = "You're looking at the list of answers."
    return HttpResponse(response)

def read_answers(request, question_id):
    response = f"You're looking at the answers to question {question_id}."
    return HttpResponse(response)

def write_answer(request, question_id):
    return HttpResponse(f"You're writing an answer to question {question_id}.")