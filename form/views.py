from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Client
from .serializers import FormSerializer,FormListSerializer
from accounts.models import CustomUser

# Create your views here.
class FormAPIView(generics.CreateAPIView):
    """
    To Create form 
    """
    serializer_class = FormSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

class FormListAPIView(generics.ListAPIView):
    """
    To display forms
    """
    model = Client
    permission_classes = [IsAuthenticated]
    serializer_class = FormListSerializer
    queryset = model.objects.all()
    