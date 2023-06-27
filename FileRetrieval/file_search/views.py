from django.shortcuts import render, redirect
from .models import Fileinfo
import os
from .forms import FolderUploadForm

def file_upload_view(request):
    if request.method == 'POST':
        form = FolderUploadForm(request.POST)
        if form.is_valid():
            folder_path = form.cleaned_data['folder_path']
            for root, _, files in os.walk(folder_path):
                for file_name in files:
                # 构建完整的文件路径
                    file_path = os.path.join(root, file_name)
                # 创建 File 对象并保存到数据库
                    file = Fileinfo(name=file_name, path=file_path)
                    file.save()
        return redirect('file_list')
    else:
        form = FolderUploadForm()
    return render(request, 'upload.html', {'form': form})

def file_list_view(request):
    files = Fileinfo.objects.all()
    context = {'files': files}
    return render(request, 'file.html', context)