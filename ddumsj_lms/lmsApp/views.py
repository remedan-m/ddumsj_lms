from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import *

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)




@api_view(['POST'])
def register_user(request):
    data = request.data

    user = User.objects.create(Id_number = data['Id_number'],
                               first_name = data['first_name'],
                               last_name = data['last_name'],
                               gender = data['gender'],
                               contact = data['contact'],
                               address = data['address'],
                               department = data['department'],
                               )
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)






@api_view(['POST'])
def register_book(request):
   pass