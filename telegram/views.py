from rest_framework import generics
from .models import Message
from .serializers import MessageSerialize

class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all().order_by('id')[:1000]
    serializer_class = MessageSerialize

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerialize