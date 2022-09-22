
from django.urls import re_path
from Photobook import views


urlpatterns = [
    re_path(r'^Photobook/$', views.Photobook_list),
    re_path(r'^Photobook/(?P<co_id>[0-9]+)$',views.Photobook_detail),
    re_path(r'^Photobook/complete$',views.Photobook_list_published),
]

# (GET)    photobook/                       - to get all the photobooks
# (GET)    photobook/<co_id>                - to get a specific order
# (POST)   photobook/                       - to add new order 
# (PUT)    photobook/<co_id>                - To update an existing Photobook
# (DELETE) photobook/<co_id>                - To remove a photobook with <co_id>
# (DELETE) photobook/                       - To remove all the orders
# (GET)    photobook/<version>              - To filter all the orders version vise 
# (GET)    photobook?order_number=[IC-1234] - To filter order_number from Photobook