from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializer, models
from rest_framework.permissions import IsAuthenticated

class TestView(APIView):
    
    async def get(self, request):
        print(request.headers)
        return Response(
            'hello world'
        )

class UsersView(ModelViewSet):
    serializer_class = serializer.UsersSerializer
    queryset = models.Users.objects.all()
    permission_classes = [IsAuthenticated]
