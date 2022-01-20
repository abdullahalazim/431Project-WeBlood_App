import email
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import DonorRegisterSerializer, DonorViewSerializer
from .models import BloodDonorProfile
from django.contrib.auth import authenticate


class RegisterView(APIView):
    def post(self, request):
        serializer = DonorRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DonorView(viewsets.ModelViewSet):
    queryset = BloodDonorProfile.objects.all().order_by('id')
    serializer_class = DonorViewSerializer


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        donor = authenticate(email=email, password=password)

        if donor:
            if donor.is_active:
                return Response({
                    "message": "success"
                })

            else:
                raise AuthenticationFailed('Donor not found')
