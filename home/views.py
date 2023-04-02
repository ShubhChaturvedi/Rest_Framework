from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
# Create your views here.

class StudentList(generics.ListCreateAPIView, generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdate(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            # token, _ = Token.objects.get_or_create(user=user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'status': 200,
                'message': 'Data Saved Successfully',
                'data': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({
            'status': 400,
            'message': 'Data Not Saved',
            'data': serializer.errors
        })
class StudentView(APIView):
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response({
            'status': 200,
            'message': 'Data Fetched Successfully',
            'data': serializer.data
        })
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                'message': 'Data Saved Successfully',
                'data': serializer.data
            })
        return Response({
            'status': 400,
            'message': 'Data Not Saved',
            'data': serializer.errors
        })
    def put(self, request, pk):
        try:
            student = Student.objects.get(id=pk)
            serializer = StudentSerializer(instance=student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Data Updated Successfully',
                    'data': serializer.data
                })
            return Response({
                'status': 400,
                'message': 'Data Not Updated',
                'data': serializer.errors
            })
        except Student.DoesNotExist:
            return Response({
                'status': 404,
                'message': 'Data Not Found'
            })
    def delete(self, request, pk):
        try:
            student = Student.objects.get(id=pk)
            student.delete()
            return Response({
                'status': 200,
                'message': 'Data Deleted Successfully'
            })
        except Student.DoesNotExist:
            return Response({
                'status': 404,
                'message': 'Data Not Found'
            })
    def patch(self, request, pk):
        try:
            student = Student.objects.get(id=pk)
            serializer = StudentSerializer(instance=student, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Data Partially Updated Successfully',
                    'data': serializer.data
                })
            return Response({
                'status': 400,
                'message': 'Data Not Partially Updated',
                'data': serializer.errors
            })
        except Student.DoesNotExist:
            return Response({
                'status': 404,
                'message': 'Data Not Found'
            })




@api_view()
def home(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response({
        'status': 200,
        'message': 'Data Fetched Successfully',
        'data': serializer.data
    })
@api_view(['POST'])
def student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'status': 200,
            'message': 'Data Saved Successfully',
            'data': serializer.data
        })
    return Response({
        'status': 400,
        'message': 'Data Not Saved',
        'data': serializer.errors
    })

@api_view(['PUT'])
def update(request, pk):
    try:
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                'message': 'Data Updated Successfully',
                'data': serializer.data
            })
        return Response({
            'status': 400,
            'message': 'Data Not Updated',
            'data': serializer.errors
        })
    except Student.DoesNotExist:
        return Response({
            'status': 404,
            'message': 'Data Not Found'
        })
@api_view(['GET'])
def get_book(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response({
        'status': 200,
        'message': 'Data Fetched Successfully',
        'data': serializer.data
    })
@api_view(['PATCH'])
def partial_update(request, pk):
    try:
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(instance=student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                'message': 'Data Updated Successfully',
                'data': serializer.data
            })
        return Response({
            'status': 400,
            'message': 'Data Not Updated',
            'data': serializer.errors
        })
    except Student.DoesNotExist:
        return Response({
            'status': 404,
            'message': 'Data Not Found'
        })

@api_view(['DELETE'])
def delete(request, pk):
    try:
        student = Student.objects.get(id=pk)
        student.delete()
        return Response({
            'status': 200,
            'message': 'Data Deleted Successfully'
        })
    except Student.DoesNotExist:
        return Response({
            'status': 404,
            'message': 'Data Not Found'
        })