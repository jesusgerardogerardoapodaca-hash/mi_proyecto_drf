from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer 
from rest_framework import status
from .models import Users
user ={
    "username": "geraapo",
    "name": "Gerardo",
    "email": "gerardo@example.com",
    "birth_day": "1990-01-30",
    "password": "123",
    "phone": "1234567890"
}
@api_view(["GET"])
def get_user(request):
    data = UserSerializer(user).data
    print(data)
    birth = data['birth_day']
    return Response(data)   


@api_view(["POST"])
def create_user(request):
    serializer_data = UserSerializer(data=request.data)
    if serializer_data.is_valid():    
        serializer_data.save()
        return Response(serializer_data.data,status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST) 

@api_view(["GET"])
def get_users(request):
    users = Users.objects.all()
    serializer_data = UserSerializer(users,many=True)
    return Response(serializer_data.data)
