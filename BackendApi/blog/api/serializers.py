from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserRegSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length = 100, write_only=True)
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            password = validated_data['password']
            
        )
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    creation_date = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Blog
        fields = ['user','id','title','content','id_category','image_url','creation_date']
    
    def get_image_url(self,obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None
    
    def get_creation_date(self, obj):
        formatted_date = obj.creation_date.strftime('%b %d, %Y')
        formatted_time = obj.creation_date.strftime('%I:%M %p')
        return f"{formatted_date} {formatted_time}"
    
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
        
        
        