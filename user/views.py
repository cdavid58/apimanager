from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User

@api_view(['POST'])
def Create_User(request):
	return Response(User.create_user(request.data))

@api_view(['GET'])
def Login_Company(request):
	return Response(User.login(request))