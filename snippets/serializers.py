from snippets.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    # # If above line not used-- user_id wil be displayed
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'language', 'style', 'owner']


class UserSerializer(serializers.ModelSerializer):
    # # Reverse relationship --> needs "related_name" --> related_name='snippet_owner' in  Snippet model
    
    # snippet_owner = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    # snippet_owner = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # snippet_owner = serializers.StringRelatedField(many=True)
    # snippet_owner = serializers.SlugRelatedField(many=True, read_only=True, slug_field='language')
    # snippet_owner = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    snippet_owner = serializers.HyperlinkedIdentityField(view_name='snippet-detail', read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'snippet_owner']



class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['title', 'duration']   

class AlbumSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    # # Reverse relationship
    track_album = TrackSerializer(many=True) # If it has related_name
    # track_album = TrackSerializer(source='track_set', many=True) # If it doesn't have related_name
    
    class Meta:
        model = Album
        fields = ['id', 'album_name', 'artist', 'owner', 'track_album']
        


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']

class CollectionSerializer(serializers.ModelSerializer):
    # If rel_name is defined or not --> It's Same in M2M
    prod_coll = ProductSerializer(read_only=True, many=True)
    # prod_coll = serializers.StringRelatedField(many=True)
    # prod_coll = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name="product-detail")
    class Meta:
        model = Collection
        fields = ['id', 'name', 'prod_coll']

class ProductCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCollection
        fields = ['id', 'is_active']