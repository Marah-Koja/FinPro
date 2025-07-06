from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Applications
from .serializers import AppSerializer 

class AppListView(APIView):
    permission_classes=[AllowAny]
    def get(self, request):
        apps = Applications.objects.all().order_by('-rating')  # الأعلى تقييمًا
        serializer = AppSerializer(apps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





