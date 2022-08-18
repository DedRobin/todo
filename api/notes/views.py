from rest_framework import viewsets, status
from rest_framework.response import Response

from api.notes.serializers import NoteSerializer
from notes.models import Note


class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed.
    """

    queryset = Note.objects.all().order_by("-created_at")
    serializer_class = NoteSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Note.objects.create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)
