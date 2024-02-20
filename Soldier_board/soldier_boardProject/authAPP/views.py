from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer


@api_view(http_method_names=['POST'])
def user_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data)
    return Response(data=serializer.errors)
