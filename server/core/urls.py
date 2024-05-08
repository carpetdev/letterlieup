from django.urls import path
from drf_spectacular.views import SpectacularAPIView
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('ping/', views.ping, name='ping'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
]

router = DefaultRouter()
router.register('questions', views.QuestionViewSet)

urlpatterns += router.urls