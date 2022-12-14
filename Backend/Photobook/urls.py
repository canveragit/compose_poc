from django.urls import re_path
from django.urls import path
from Photobook import views
from django.conf import settings 
from django.conf.urls.static import static 

app_name = "Photobook"

urlpatterns = [
    # path("",views.index), # Not needed anymore
    path("upload",views.OrderUpload,name="uploads"),
    re_path(r'^Photobook$', views.Photobook_list),
    re_path(r'^Photobook/(?P<co_id>[0-9]+)$',views.Photobook_detail),
#    re_path(r'^Photobook/complete$',views.Photobook_list_published),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# (GET)    photobook                        - to get all the photobooks
# (GET)    photobook/<co_id>                - to get a specific order
# (POST)   photobook                        - to add new order 
# (PUT)    photobook/<co_id>                - To update an existing Photobook
# (DELETE) photobook/<co_id>                - To remove a photobook with <co_id>
# (DELETE) photobook                        - To remove all the orders
# (GET)    photobook/<version>              - To filter all the orders version vise 
# (GET)    photobook?order_number=[IC-1234] - To filter order_number from Photobook

# (POST)   				        - index.html
# (POST)   upload			    - To upload images to ImageAlbum table in DB with the orderID and FileName
