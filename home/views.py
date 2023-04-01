from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
# Create your views here.


class StudentView(APIView):
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