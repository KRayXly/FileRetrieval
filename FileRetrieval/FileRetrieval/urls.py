"""
URL configuration for FileRetrieval project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.urls import path
# from FileRetrieval import view

# urlpatterns = [
#     path("upload/", view.mainpage),
#     path("view/",view.upload),
# ]
from django.contrib import admin
from django.urls import path
from file_search.views import file_upload_view, search_view , save_results

urlpatterns = [
    path('', file_upload_view, name='file_upload'),
    path('search/', search_view, name='search'),
    path('save_results/', save_results, name='save_results'),
]