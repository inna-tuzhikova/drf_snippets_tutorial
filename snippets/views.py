from django.http import Http404
from rest_framework import status, mixins, generics
from rest_framework.response import Response

from .models import Snippet
from .serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
    """Lists all snippets, or creates a new snippet"""
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieves, updates or deletes a snippet instance"""
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
