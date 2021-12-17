from rest_framework import serializers
from mag.models import *


class addContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('senderName', 'senderEmail',
                  'senderMessage', 'status')


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'date', 'tag', 'sku', 'excerpt')
