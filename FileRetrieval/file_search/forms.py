from django import forms

class FolderUploadForm(forms.Form):
    # folder = forms.FileField(widget=forms.ClearableFileInput(attrs={'webkitdirectory': True, 'directory': True}))
    # folder = forms.FileField(
    #     label='选择需要上传的文件夹 ',
    #     widget=forms.ClearableFileInput(attrs={'webkitdirectory': True, 'directory': True , 'class':'form-control'}))
    folder_path = forms.CharField(label='文件夹路径')