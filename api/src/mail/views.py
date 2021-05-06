from rest_framework import views, status
from rest_framework.response import Response
from mail.serializers import EmailSerializer
from mail.services import send_email


class MailView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        send_email(**serializer.validated_data)
        return Response({'message': 'Message sent successfully'})