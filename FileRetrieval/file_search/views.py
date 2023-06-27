from django.shortcuts import render, redirect
from .models import UploadFile
import zipfile
from .forms import FolderUploadForm

def file_upload_view(request):
    if request.method == 'POST':
        form = FolderUploadForm(request.POST, request.FILES)
        if form.is_valid():
            folder = form.cleaned_data['folder']
            files = request.FILES.getlist('files')
            for file in files:
                UploadFile.objects.create(folder=folder, file=file)
            return redirect('file_list')
    else:
        form = FolderUploadForm()
    context = {'form': form}
    return render(request, 'upload.html', context)

def file_list_view(request):
    files = UploadFile.objects.all()
    context = {'files': files}
    return render(request, 'file.html', context)