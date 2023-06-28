# from multiupload.fields import MultiFileField
# from django import forms


# class UploadFileForm(forms.Form):
#     folder = forms.CharField(max_length=255)
#     files = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)

from django import forms

class FolderUploadForm(forms.Form):
    folder = forms.FileField(
        label='选择需要上传的文件夹 ',
        widget=forms.ClearableFileInput(attrs={'webkitdirectory': True, 'directory': True , 'class':'form-control'}))