from django.http import HttpResponse,FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from django.contrib.auth.models import User
# Create your views here.

@api_view(['GET','POST'])
def home(request):
    blog = Blog.objects.all()
    serialize = BlogSerializer(blog,many=True, context={'request':request})
    
    return Response(serialize.data)

@api_view(['GET'])
def postdetails(request,pk):
    post = Blog.objects.get(pk=pk)
    serialize = BlogSerializer(post, context={
        'request':request,
    })
    return Response(serialize.data)



@api_view(['GET'])
def category(request):
    category = Category.objects.all()
    serialize = CategorySerializer(category,many=True)
    
    return Response(serialize.data)


@api_view(['GET'])
def users(request):
    user = User.objects.all()
    serialize = UserSerializer(user,many=True)
    
    return Response(serialize.data)

@api_view(['POST'])
def user_registration(request):
    serializer = UserRegSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    return Response(serializer(serializer.errors, status=status.HTTP_400_BAD_REQUEST))



