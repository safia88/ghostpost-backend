from rest_framework import serializers
from api.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ["content", "is_boast", "up_votes", "down_votes",
                  "total_votes", "submit_time", "secret_key", 'id']
