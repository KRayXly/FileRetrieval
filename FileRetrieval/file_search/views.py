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
    if request.method == 'POST':
        form = FolderUploadForm(request.POST)
        if form.is_valid():
            folder_path = form.cleaned_data['folder_path']
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
        return render(request, 'upload.html',context)
    else:
       Fileinfo.objects.all().delete()
    return render(request, 'upload.html', context)

def file_list_view(request):
    files = Fileinfo.objects.all()
    context = {'files': files}
    return render(request, 'file.html', context)


def search_view(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        # 在这里执行根据关键字搜索的逻辑
        # 这里仅作示例，搜索当前目录下所有文件名包含关键字的文件
        current_dir = os.getcwd()
        results = []
        for root, dirs, files in os.walk(current_dir):
            for file in files:
                if keyword in file:
                    file_path = os.path.join(root, file)
                    results.append(file_path)
        return render(request, 'file.html', {'results': results, 'keyword': keyword})
    else:
        return render(request, 'file.html')

def save_results(request):
    if request.method == 'POST':
        selected_files = request.POST.getlist('selected_files')
        # 在这里执行保存选中结果的逻辑
        # 这里仅作示例，将选中的文件路径保存到文本并返回下载
        file_content = '\n'.join(selected_files)
        response = HttpResponse(content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="search_results.txt"'
        response.write(file_content)
        return response