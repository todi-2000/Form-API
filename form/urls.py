from django.urls import path, include
from .views import FormAPIView, FormListAPIView

urlpatterns = [
    path('fill/',FormAPIView.as_view()),
    path('view/',FormListAPIView.as_view())
]
