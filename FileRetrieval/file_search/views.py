#-*- coding: utf-8 -*-

from http.client import HTTPResponse
import shutil
from django.shortcuts import render, redirect
from .models import Fileinfo
import os
from .forms import FolderUploadForm

#设置过滤后的文件类型 当然可以设置多个类型
filter=[".txt",".doc",".pdf",".docx"]
def file_upload_view(request):
    form = FolderUploadForm()
    files = Fileinfo.objects.all()
    context = {'files': files,'form': form}
    if os.path.exists('upload'):
        shutil.rmtree('upload')
    Fileinfo.objects.all().delete()
    if request.method == 'POST':
        form = FolderUploadForm(request.POST, request.FILES)
        if form.is_valid():
            folder = request.FILES.getlist('folder')
            # 创建文件夹的路径
            folder_path = os.path.join('upload')
            # 确保文件夹目录存在
            os.makedirs(folder_path, exist_ok=True)
            # 遍历上传的文件夹内的所有子文件夹和文件，并将文件逐个保存到服务器
            for file in folder:
                destination_path = os.path.join(folder_path, file.name)
                with open(destination_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
            for root, _, files in os.walk(folder_path):
                for file_name in files:
                    # 构建完整的文件路径
                    file_path = os.path.join(root, file_name)
                    #获取文件后后缀
                    ext = os.path.splitext(file_path)[1]
                    if ext in filter:
                    # 创建 File 对象并保存到数据库
                        file = Fileinfo(name=file_name, path=file_path)
                        file.save()
        # return render(request, 'upload.html',context)
    else:
       form = FolderUploadForm()
       Fileinfo.objects.all().delete()
    return render(request, 'upload.html', context)

def search_view(request):
    results = []
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        form = FolderUploadForm()
        files = Fileinfo.objects.all()
        context = {'files': files,'form': form,'results':results}
        # 在这里执行根据关键字搜索的逻辑
        for file in files:
            filepath=file.path
            ext = os.path.splitext(filepath)[1]
            if ext=='.txt':
                with open(filepath, 'r',encoding='UTF-8') as file:
                    for line in file:
                        if keyword in line:
                            results.append(line)
    return render(request, 'upload.html', context)

def save_results(request):
    if request.method == 'POST':
        selected_files = request.POST.getlist('selected_files')
        # 在这里执行保存选中结果的逻辑
        # 这里仅作示例，将选中的文件路径保存到文本并返回下载
        file_content = '\n'.join(selected_files)
        response = HTTPResponse(content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="search_results.txt"'
        response.write(file_content)
        return response