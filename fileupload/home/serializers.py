from rest_framework import serializers
from .models import Folder , Files
import shutil


class FileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Files
        fields = '__all__'


class FileListSerializer(serializers.Serializer):
    
    file = serializers.ListField(
        child = serializers.FileField(max_length =100000, allow_empty_file=False, use_url = False)
    )
    folder = serializers.CharField(required = False)
    
    
    def zip_file(self, folder):
        
        # shutil.make_archive('outputfile location' , 'zip', 'directrory name')
        
        shutil.make_archive(f'media/{folder}' , 'zip', f'media/{folder}')
    
    def create(self, validated_data):
        folder = Folder.objects.create()
        file = validated_data.pop('file')
        print(file)
        files_objs = []
        for f in file:
            files_obj = Files.objects.create(folder = folder,file = f)
            files_objs.append(files_obj)
            
        self.zip_file(folder.uid)
            
        return {"file": {}, 'folder': str(folder.uid)}