from rest_framework import serializers

from ..models import Publication


class BaseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)


class PublicationSerializer(BaseSerializer):
    """Publication Serializer"""

    class Meta:
        model = Publication
        fields = ('id', 'date', 'subject', 'content')
