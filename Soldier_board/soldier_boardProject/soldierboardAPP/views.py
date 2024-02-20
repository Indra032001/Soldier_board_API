from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import SBoard
from .serializers import BoardSerializers


@api_view(http_method_names=['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def Board_Api(request):
    if request.method == "POST":
        serializer_obj = BoardSerializers(data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(data=serializer_obj.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    model_obj = SBoard.objects.all()
    serializer_obj = BoardSerializers(model_obj, many=True)
    return Response(data=serializer_obj.data, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def Board_detailed_Api(request, id=None):
    soldier = get_object_or_404(SBoard, id=id)

    if request.method == 'GET':
        serializer_obj = BoardSerializers(soldier)
        return Response(data=serializer_obj.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer_obj = BoardSerializers(data=request.data, instance=soldier)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(data=serializer_obj.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer_obj.data, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        serializer_obj = BoardSerializers(data=request.data, instance=soldier, partial=True)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(data=serializer_obj.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer_obj.data, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        soldier.delete()
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)
