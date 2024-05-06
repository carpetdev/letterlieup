from django.urls import path

from . import views

urlpatterns = [
    path('ping', views.ping, name='ping'),
    path('list/', views.list_answers, name='list_answers'),
    path('answers/<int:question_id>/', views.read_answers, name='read_answers'),
    path('write/<int:question_id>/', views.write_answer, name='write_answer'),
]