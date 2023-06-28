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