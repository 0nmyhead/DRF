# from rest_framework import serializers
# from blog.models import Blog

# class BlogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Blog
#         fields = '__all__'
from .models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.login_id')
    class Meta:
        model = Blog
        fields = ['id', 'title', 'created_at', 'user', 'body']