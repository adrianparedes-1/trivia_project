from django.views import View
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse
from . import serializer, models
from rest_framework.permissions import IsAuthenticated

class TestView(View):
    
    def get(self, request):
        print(request.headers)
        return HttpResponse(
            'hello world'
        )

class UsersView(ModelViewSet):
    serializer_class = serializer.UsersSerializer
    queryset = models.Users.objects.all()
    permission_classes = [IsAuthenticated]