from django import forms

class FolderUploadForm(forms.Form):
    # folder = forms.FileField(widget=forms.ClearableFileInput(attrs={'webkitdirectory': True, 'directory': True}))
    folder_path = forms.CharField(label='文件夹路径')