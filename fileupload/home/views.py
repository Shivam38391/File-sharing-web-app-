from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import FileListSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

# Create your views here.



class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return


def home(request):
    
    # if request.method == "POST":
        
        # files = request.FILES
        # data = request.data
        # print(files)
        # print("DATA FILES",data)
        
    
    return render(request, "home/home.html")

class HandleFileUpload(APIView):
    parser_classes = [MultiPartParser,FormParser]
    # parser_classes = [FileUploadParser]
    permission_classes = ()
    # authentication_classes = (CsrfExemptSessionAuthentication,)

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


