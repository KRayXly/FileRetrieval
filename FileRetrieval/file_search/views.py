#-*- coding: utf-8 -*-
import json
import psutil
from http.client import HTTPResponse
from django.http import HttpResponse
from django.http import JsonResponse
import shutil
from django.shortcuts import render, redirect
from .models import Fileinfo
import os
from .forms import FolderUploadForm
import docx
import PyPDF2
from django.views.decorators.csrf import csrf_exempt

#设置过滤后的文件类型 当然可以设置多个类型
filter=[".txt",".doc",".pdf",".docx"]
def file_upload_view(request):
    # 获取本地磁盘路径列表
    disk_paths = get_local_disk_paths()
    # 将磁盘路径列表传递给模板
    context = {
        'disk_paths': disk_paths
    }
    if request.method == 'POST':
        # 处理文件上传逻辑
        # 获取选择的磁盘路径
        disk = request.POST.get('disk')
        # 获取下一级目录
        top_level_directories = get_top_level_directories(disk)
        # 将目录列表传递给模板
        context['top_level_directories'] = top_level_directories
    return render(request, 'upload.html', context)
def file_upload2(request):
    file_path = request.POST.get('file_path')
    print('File Path:', file_path)
    if file_path is not None:
        print('File Path:', file_path)
        return HttpResponse('File Path: ' + file_path)
    else:
        # 处理未提供file_path的情况
        return HttpResponse('File Path is missing')


def search_view(request):
    results = []
    results2 = []
    # results3 = []
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        form = FolderUploadForm()
        files = Fileinfo.objects.all()
        context = {'files': files,'form': form,'results':results,'results2':results2,'keyword': keyword}
        # 在这里执行根据关键字搜索的逻辑
        for file in files:
            filepath=file.path
            filename=file.name
            ext = os.path.splitext(filepath)[1]
            #对txt文件按行进行关键字匹配
            if ext=='.txt':
                flag=0
                with open(filepath, 'r',encoding='UTF-8') as file:
                    tnum=0
                    for (tnum,line) in enumerate(file):
                        tnum=tnum+1
                        if keyword in line:
                            if flag==0:
                                results2.append(filename)
                                #将关键字进行高亮显示
                                highlighted_line=line.replace(keyword, f"<span style='color: red'>{keyword}</span>")
                                txt=Result(filename,str(tnum),highlighted_line)
                                results.append(txt)
                                flag=1
                            else:
                                #将关键字进行高亮显示
                                highlighted_line=line.replace(keyword, f"<span style='color: red'>{keyword}</span>")
                                txt=Result(filename,str(tnum),highlighted_line)
                                results.append(txt)
            #对pdf文件按行进行关键字匹配                
            elif ext=='.pdf':
                flag=0
                with open(filepath, 'rb') as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    page_count = len(pdf_reader.pages)
                    pnum=0
                    for page_num in range(page_count):
                        page = pdf_reader.pages[page_num]
                        text = page.extract_text()
                        lines = text.split('\n')
                        for line in lines:
                            pnum=pnum+1
                            if keyword in line:
                                if flag==0:
                                    results2.append(filename)
                                    #将关键字进行高亮显示
                                    highlighted_line=line.replace(keyword, f"<span style='color: red'>{keyword}</span>")
                                    txt=Result(filename,str(pnum),highlighted_line)
                                    results.append(txt)
                                    flag=1
                                else:
                                    #将关键字进行高亮显示
                                    highlighted_line=line.replace(keyword, f"<span style='color: red'>{keyword}</span>")
                                    txt=Result(filename,str(pnum),highlighted_line)
                                    results.append(txt)
            #对word文件按段落进行关键字匹配                     
            elif ext=='.docx':
                flag=0
                doc = docx.Document(filepath)
                dnum=0
                for paragraph in doc.paragraphs:
                    dnum=dnum+1
                    content=paragraph.text
                    if keyword in content:
                        if flag==0:
                            results2.append(filename)
                            #将关键字进行高亮显示
                            highlighted_text=content.replace(keyword, f"<span style='color: red'>{keyword}</span>")
                            txt=Result(filename,str(dnum),highlighted_text)
                            results.append(txt)
                            flag=1
                        else:
                            #将关键字进行高亮显示
                            highlighted_text=content.replace(keyword, f"<span style='color: red'>{keyword}</span>")
                            txt=Result(filename,str(dnum),highlighted_text)
                            results.append(txt)
    return render(request, 'upload.html', context)

def save_results(request):
    if request.method == 'POST':
        selected_rows = json.loads(request.body.decode('utf-8'))['selected_rows']
        
        result_text = []
        for row in selected_rows:
            result_text.append(row)  # 添加选中行的内容

        result_text = '\n'.join(result_text)
        response = HttpResponse(result_text, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="selected_results.txt"'
        return response
    
#定义Result类保存搜索出的包含关键字的行
class Result:
    def __init__(self,path, num,name):
        self.path=path
        self.name = name
        self.num = num

def get_local_disk_paths():
    # 获取本地磁盘路径列表
    disk_partitions = psutil.disk_partitions()
    local_disk_paths = []
    for partition in disk_partitions:
        if 'cdrom' not in partition.opts and partition.fstype != '':
            local_disk_paths.append(partition.mountpoint)
    return local_disk_paths

def get_top_level_directories(request):
    directory = request.GET.get('directory')
    directories = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            directories.append(item)
    return JsonResponse({'directories': directories})

def getpathview(request):
    folder_path=request.GET.get('value')
    print(folder_path)
    Fileinfo.objects.all().delete()
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
    files = Fileinfo.objects.all()
    return render(request, 'upload.html',{'files': files,'ffpath':folder_path})

