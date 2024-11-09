from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Users,Authors,Articles,Comments
from .serializer import UsersSerializer,AuthorsSerializer,ArticlesSerializer,CommentsSerializer

# Create your views here.

# HTTP REQUEST GET,POST,PUT,DELETE
# apis to interact with users model
@api_view(['GET'])
def get_users(request):
    users = Users.objects.all()
    serializer = UsersSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def user_detail(request,pk):
    try:
        user=Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UsersSerializer(user)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = UsersSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# api to interact with Authors model
@api_view(['GET'])
def get_authors(request):
    authors = Authors.objects.all()
    serializer = AuthorsSerializer(authors,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_author(request):
    serializer = AuthorsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def author_detail(request,pk):
    try:
        author=Authors.objects.get(pk=pk)
    except Authors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AuthorsSerializer(author)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = AuthorsSerializer(author,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# api to interact with Article model
@api_view(['GET'])
def get_articles(request):
    article = Articles.objects.all()
    serializer = ArticlesSerializer(article,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_article(request, author_id):
    try:
        author = Authors.objects.get(pk=author_id) 
    except Authors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = request.data.copy()
    data['author'] = author.id
    serializer = ArticlesSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def single_article(request,author_id):
    try:
        article=Articles.objects.get(pk=author_id)
    except Authors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ArticlesSerializer(article)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = ArticlesSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# api to interact with Comments model
@api_view(['GET'])
def get_comments(request):
    comment = Comments.objects.all()
    serializer = CommentsSerializer(comment,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_comment(request,article_id):
    try:
        article = Articles.objects.get(pk=article_id)
    except Articles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = request.data.copy()
    data['article'] = article.id
    serializer = CommentsSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def single_comment(request,pk):
    try:
        comment=Comments.objects.get(pk=pk)
    except Comments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CommentsSerializer(comment)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = CommentsSerializer(comment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
