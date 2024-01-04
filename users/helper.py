# get file url for request file saving this to profile img foler 
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def save_image_file_get_url(request, file):
    file_name = file.name
    file_content = ContentFile(file.read())
    file_path = default_storage.save(f'static/profile_img/{file_name}', file_content)
    url =  request.build_absolute_uri(f'{file_path}')
    return url
    
    