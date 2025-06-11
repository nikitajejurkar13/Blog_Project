from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from .authentication import CustomJWTAuthentication

class CreatePostView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'message': 'Post created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ListPostsView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, post_id=None):
        if post_id:
            post = get_object_or_404(Post, id=post_id, user=request.user)
            serializer = PostSerializer(post)
            return Response(serializer.data, status=200)
        else:   
            post = Post.objects.all()
            serializer = PostSerializer(post , many=True)
            return Response(serializer.data, status=200)
    
    def put(self, request, post_id=None):

        if not post_id:
            return Response({"detail": "Post ID is required for update."}, status=400)

        post = get_object_or_404(Post, id=post_id, user=request.user)
        serializer = PostSerializer(post, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, post_id=None):
        if not post_id:
            return Response({"detail": "Post ID is required for deletion."}, status=400)

        post = get_object_or_404(Post, id=post_id, user=request.user)
        post.delete()
        return Response({"detail": "Post deleted successfully"}, status=204)

    