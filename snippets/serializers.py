from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_framework import serializers


# SnippetSerializer class is replicating a lot of information that's also contained in the Snippet model.
# It would be nice if we could keep our code a bit more concise.

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'language', 'style']
