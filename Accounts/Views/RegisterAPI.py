# from knox.models import AuthToken
# from rest_framework import generics
# from rest_framework.response import Response
#
# from Accounts.Serializer.RegisterSerializer import RegisterSerializer
# from Accounts.Serializer.UserDetailSerializer import UserDetailSerializer
#
#
# class RegisterAPI(generics.GenericAPIView):
#     serializer_class = RegisterSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#             "user": UserDetailSerializer(user, context=self.get_serializer_context()).data,
#             "token": AuthToken.objects.create(user)[1]
#         })
#
