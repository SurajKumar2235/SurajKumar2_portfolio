from rest_framework.views import APIView
from django.shortcuts import render, redirect
from .forms import ContactForm
from .serializers import ProjectsSerializer,ContactSerializer

class HomeView(APIView):
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, 'portfolio/home.html')

class ContactAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        print("-------------------")
        if serializer.is_valid():
            
            serializer.save()
            return Response({'message': 'Your message has been sent successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Projects

class ProjectsAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Default permission class


    def get(self, request):   # get all the data and send to the server
        projects = Projects.objects.all()
        serializer = ProjectsSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request):   # add new project
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):# edit project detail
        project = Projects.objects.get(pk=pk)
        serializer = ProjectsSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):# delete the project
        project = Projects.objects.get(pk=pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]  # Allow unrestricted access for GET requests
        return super().get_permissions()