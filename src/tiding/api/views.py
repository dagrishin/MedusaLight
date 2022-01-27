from rest_framework import filters
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializer import PublicationSerializer
from src.tiding.models import Publication


class PublicationView(ReadOnlyModelViewSet):
    """Publication View"""
    queryset = Publication.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PublicationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['subject', 'content', '@subject', '@content']
