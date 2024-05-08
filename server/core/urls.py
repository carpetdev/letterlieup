from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('ping/', views.ping, name='ping'),
]

router = DefaultRouter()
router.register('', views.QuestionViewSet)

urlpatterns += router.urls