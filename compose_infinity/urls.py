"""compose_infinity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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


# from django.conf.urls import url,include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url(r'^',include('Photobook.urls'))
# ]
from django.contrib import admin
from django.urls import path

from django.urls import include, re_path
from Photobook.views import add_PhotobookAPI,update_photobook

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^Photobook/add-order$',add_PhotobookAPI),
    re_path(r'^Photobook/(?P<co_id>[^/]*)/$', update_photobook),
    re_path(r'^Photobook/([0-99]+)$',update_photobook),
    
    # re_path(r'^Photobook/add-order$', PhotobookAPI, name='PhotobookAPI'),
    # re_path(r'^Photobook/add-order$', include('Photobook.urls')),
]