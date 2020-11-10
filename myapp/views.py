from django.shortcuts import render

from .models import Blog

from rest_framework import viewsets
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('__all__')

class BlogModelViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.order_by('-created_at')