from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def index(request):
    # user = request.data.get("user_email")
    # tokens = request.data.get("token_amount")
    # return Response({
    #     "user_email": user,
    #     "token_amount": tokens
    # })
    return Response(request.data)