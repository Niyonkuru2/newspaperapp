from rest_framework import serializers
from .models import Users,Articles,Authors,Comments
class UsersSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Users
        fields = '__all__'
class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'