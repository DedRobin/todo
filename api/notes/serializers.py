from rest_framework import serializers


class NoteSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    text = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    # author_id = serializers.IntegerField()
