from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from .models import *

@api_view(['POST'])
def for_test(request):
    print(request.data["data"])
    try: 
        query = For_test(is_true=request.data["data"])
        query.save()
        return Response({'code': f'request processed {status.HTTP_200_OK}'})
    except ValidationError:
        return Response({'code': f'request was rejected {status.HTTP_400_BAD_REQUEST}'})