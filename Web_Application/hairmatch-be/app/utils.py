import os

def save_uploaded_file(image):
    os.makedirs('./app/uploads', exist_ok=True)
    file_path = os.path.join('./app/uploads', image.filename)
    image.save(file_path)
    return file_path

def clean_up_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
