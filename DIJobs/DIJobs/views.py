import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

from .serializers import UserSerializer

logger = logging.getLogger(__name__)

class UserDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    # def patch(self, request):
    #     logger.info("Received PUT request to update user profile")
    #     logger.debug("Request data: %s", request.data)
    #     serializer = UserSerializer(request.user, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         logger.info("Serializer is valid, saving user profile")
    #         serializer.save()
    #         logger.debug("Updated user data: %s", serializer.data)
    #         return Response(serializer.data)
    #     logger.error("Serializer is invalid: %s", serializer.errors)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

