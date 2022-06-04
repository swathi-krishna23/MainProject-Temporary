from django.core.files.storage import FileSystemStorage
from model.RunCamera import sendToBk

def handle_uploaded_file(file): 
    fs = FileSystemStorage()
    filename = fs.save(file.name, file)
    uploaded_file_path = fs.path(filename)
    print('absolute file path', uploaded_file_path)
    sendToBk(uploaded_file_path)