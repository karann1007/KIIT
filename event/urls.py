"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path

import event
from restapi.views import create_event, delete_event, event_fetch_id, filter_event, update_event

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/event/', create_event),
    path('api/event/update/', update_event),
    path('api/event/filter/', filter_event),
    path('api/event/single/', event_fetch_id),
    path('api/event/', delete_event),
]
