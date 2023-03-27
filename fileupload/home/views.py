from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import FileListSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FileUploadParser ,FormParser
# Create your views here.

class HandleFileUpload(APIView):
    parser_classes = [MultiPartParser,FormParser]
    # parser_classes = [FileUploadParser]

    def post(self, request):

        # try:
        data = request.FILES
        print(data)
        serializer = FileListSerializer(data= data)
        print("after serializer",serializer)  
        if serializer.is_valid():
            serializer.save()
            print("serializers.data === to ",serializer.data)  
            
            return Response({"status": 200,"message": "success", 'data' : serializer.data},status=status.HTTP_200_OK)
            
        else:
            print("not validated",data)  
            print(serializer.is_valid())
            return Response({"status":400,'data': serializer.errors },status = status.HTTP_400_BAD_REQUEST)
            
        # except:
        #     return Response({"status":400, "message":  "in exception block"},status = status.HTTP_400_BAD_REQUEST)
