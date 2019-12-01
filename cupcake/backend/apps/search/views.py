from rest_framework.response import Response
from rest_framework.views import status, APIView
from rest_framework import permissions, authentication

from .serializer import PersonSerializer
from apps.utils.elasticsearch import Service


class PersonView(APIView):
    """View to list all person register"""

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, format=None):
        service_es = Service()
        json = self.request.data
        response = service_es.send_request(path='person/_search', json=json)
        sanitizer_data = service_es.sanitizer_query(response)
        serializer = PersonSerializer(sanitizer_data, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
