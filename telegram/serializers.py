from rest_framework import serializers
from .models import Message

class MessageSerialize(serializers.ModelSerializer):

    class Meta:
        model = Message
        # fields = ('id', 'contextid', 'date', 'fromid', 'message', 'replymessageid', 'forwardid', 'postauthor', 'viewcount', 'mediaid', 'formatting', 'serviceaction',)
        fields = ('id', 'contextid', 'date', 'message', 'replymessageid', 'forwardid', 'postauthor', 'viewcount', 'formatting', 'serviceaction',)
        