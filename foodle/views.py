from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .models import BlogPost
from . import serializers
from .permissions import ReadOnly
from django.views.generic import TemplateView



def index(request, path=''):
    """
    The home page. This renders the container for the single-page app.
    """
    return render(request, 'index.html')

def about(request, path='./about'):
    """
    The home page. This renders the container for the single-page app.
    """
    return render(request, 'about.html')

# class AboutPageView(TemplateView):
#    

#   def get(self, request, **kwargs):
#      return render(request, 'about.html', context=None) */

class UserViewSet(viewsets.ModelViewSet):
    """
    Provides basic CRUD functions for the User model
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (ReadOnly, )


class BlogPostViewSet(viewsets.ModelViewSet):
    """
    Provides basic CRUD functions for the Blog Post model
    """
    queryset = BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
