import os
from django.db import models
import uuid

# Create your models here.
class Folder(models.Model):
    
    uid = models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    
    

    # dynamic folder creation

def get_upload_path(instance, filename):
        return os.path.join(str(instance.folder.uid), filename)

    


class Files(models.Model):

    
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_path)
    created_at = models.DateTimeField(auto_now =True)
    
    def __str__(self):
        # return str(self.folder.uid) + str(self.created_at)
        return f'FOLDER NAME is {self.folder.uid} AND UPLOADED ON {self.created_at}'

            # f'folder name is {self.folder.uid}and uploaded on {self.created_at}'

