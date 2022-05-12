from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Message
from .serializers import MessageSerializer

class MessagesApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # Get all messages
    def get(self, request, *args, **kwargs):
        messages = Message.objects.all().order_by('sent_at')
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Send message
    def post(self, request, *args, **kwargs):
        data = {
            'text': request.data.get('text'), 
            'email': request.user.email,
        }
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
