from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import PostSerializer
from api.models import Post

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-submit_time')
    serializer_class = PostSerializer

    @action(detail=False)
    def boast(self, request):
        posts = Post.objects.filter(is_boast=True).order_by('-submit_time')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roast(self, request):
        posts = Post.objects.filter(is_boast=False).order_by('-submit_time')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def sorted_posts(self, request):
        #posts = Post.objects.order_by('-total_votes')
        posts = Post.objects.all().order_by('-up_votes', 'down_votes')
        seriallizer = self.get_serializer(posts, many=True)
        return Response(seriallizer.data)

    @action(detail=True, methods=['post'])
    def up_vote(self, request, pk=id):
        post = Post.objects.get(pk=pk)
        post.up_votes += 1
        post.save()
        return Response('success')

    @action(detail=True, methods=['post'])
    def down_vote(self, request, pk=id):
        post = Post.objects.get(pk=pk)
        post.down_votes += 1
        post.save()
        return Response('success')

    @action(detail=True, methods=['post'])
    def delete_post(self, request, pk=id):
        instance = Post.objects.get(secret_key=pk)
        instance.delete()
        return Response('success')
