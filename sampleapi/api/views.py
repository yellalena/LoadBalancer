import uuid

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ratelimit.decorators import ratelimit


class HelloView(APIView):
    @ratelimit(key='ip', rate='5/s', block=True)
    def get(self, request):
        return Response({"msg":"hello back"}, status=status.HTTP_200_OK)
