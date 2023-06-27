# Django运行
        python manage.py runserver
        出现报错：
        pip install django-multiupload//下载对应module

# github操作方法
## （B端）如何下载
        git clone https://github.com/KRayXly/FileRetrieval.git

## 提交代码到仓库
        git add . //添加文件到本地仓库
        git branch -M main //选择main分支，可以改名上传其它分支
        git commit -m "姓名 学号" //添加文件描述信息
        git remote add origin https://github.com/KRayXly/FileRetrieval.git //链接远程仓库，创建主分支
        git push -u origin main //此处上传的是main分支
  
## （A端）获取远程仓库更新
        git pull origin main

## 注意点
- 对整个大文件夹（文件夹内包括FileRetrieval文件夹和两份md文件的文件夹）进行git bush
- 不要使用任何带 -f 的语言

## 可能出现的错误
- error: remote origin already exists.

解决方法：

        git remote rm origin //先删除远程 Git 仓库

        git remote add origin xxx //再添加远程 Git 仓库

- error: OpenSSL SSL_read: Connection was reset, errno 10054
  
解决方法：

        git config --global http.sslVerify "false"

如果不行，就在C:\Windows\System32\drivers\etc里的hosts文件的最后一行添加：140.82.114.4 github.com
（使用vscode打开）

- Failed to connect to github.com port 443: Timed out

解决方法：

        git config --global --unset http.proxy

