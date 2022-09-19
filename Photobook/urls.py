
from crypt import methods
from django.urls import include, re_path
from Photobook import views


urlpatterns = [
    re_path(r'^Photobook/add-order$',views.add_PhotobookAPI),
    re_path(r'^Photobook/(?P<co_id>[^/]*)/$', views.update_photobook),
    re_path(r'^Photobook/([0-99]+)$',views.update_photobook),
    # re_path(r'^Photobook/([0-99]+)$',views.PhotobookAPI)
]
