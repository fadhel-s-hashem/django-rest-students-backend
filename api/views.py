#  necesary tamplet for the viewrs (controller)
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404

# import the models and serializer
from .models import Student
from .serializers import StudentSerializer

@api_view(["GET", "POST"])
def student_list_create(request):
    if request.method == "GET":
        # 1. Query all Student records.
        students = Student.objects.all()
        # 2. Serialize the collection with many=True.
        serializer = StudentSerializer(students,many=True)
        # 3. Return the serializer data.
        return Response(serializer.data)


    # 1. Build a serializer with data=request.data.
    serializer = StudentSerializer(data=request.data)
    # 2. Validate it.
    if serializer.is_valid():
        # 3. Save and return the new object with 201 Created.
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # 4. Return validation errors with 400 Bad Request.
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
Why many=True? The GET branch serializes a collection. The POST branch handles one incoming object, so it must not use many=True.
'''

@api_view(["GET", "PUT", "DELETE"])
def student_detail(request, student_id):
    # Find the student or return 404.
    '''
    use this so if there no match route appear error
    '''
    student= get_object_or_404(Student, pk=student_id)

    if request.method == "GET":
        # Serialize and return one student.
        Serializer = StudentSerializer(student)
        return Response(Serializer.data)

    if request.method == "PUT":
        serializer = StudentSerializer(student, data= request.data)
        # Validate request.data against the existing instance.
        if serializer.is_valid():
            serializer.save()
        # Return the updated object or validation errors.
            return Response(serializer.data)
        
    # Save the ID as a string, delete the instance, and return JSON.
        deleted_id = str(student.id)
        student.delete()
        return Response ({"message" : "student deleted", "_id": deleted_id})

