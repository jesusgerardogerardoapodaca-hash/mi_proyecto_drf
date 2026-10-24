from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer 

user ={
    "name": "Gerardo",
    "password": "123"
}
@api_view(["GET"])
def get_users(request):
    return Response(UserSerializer(user).data)