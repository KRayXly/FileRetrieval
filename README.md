# 暑假实训 FileRetrieval
Short term document retrieval project
- KRayXly 林之韵 2019211910020
- Xlanalili 王若澜 2020212205128
- Jiney88 金凤 2019210308034

## 答辩要求

- online: 给出访问域名地址 'https://github.com/KRayXly/FileRetrieval'
- PPT & 演示 (5分钟)
- 答辩时分别展示：PPT、功能、性能、内存，并且给出源代码地址


## 技术框架
- Language: Python(Django)
- Database: MySQL
- Page: H5 + CSS
- Server: GIT

### 页面框架

```
- FileRetrival
    - file_search 
        - static 静态资源/css
        - templates 网页文件/html
        - views.py 添加的视图文件
        - models.py 模型调用数据库
        - forms.py 表单相关
    - FileRetrival 项目容器，存放Django项目配置
```

## 项目命题

要求实现一个APP文件检索系统，具体描述如下：

1. 选择硬盘一个文件夹作为查询的目录，此时将该目录下的所有检索文件 `pdf`/`word` 建立索引，保存到数据库中；
2. 输入查询的关键字，将符合要求的结果按下面格式显示出来
3. 点击选择多个查询结果内容，在点击保存可以将数据保存到文本，并下载。

```
路径A\子路径B\...\文件1      
-------------------------------
行号x    包括关键字的内容行   
行号y    包括关键字的内容行
...
行号z    包括关键字的内容行


路径C\子路径D\...\文件2     
-------------------------------
行号x    包括关键字的内容行   
行号y    包括关键字的内容行
...
行号z    包括关键字的内容行


......