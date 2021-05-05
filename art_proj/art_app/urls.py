from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('login_reg', views.login_reg), # render registration template
    path('process_reg', views.process_reg), # adds user to DB
    path('login', views.login), # log in, gets user from DB then redirect to sucsess
    path('sucsess', views.sucsess), # to render appropriate template for artist/customer
    path('add_item', views.add_item), # renders add item page for artist
    path('create_art', views.create_art), # adds artwork to DB
    path('add_item_img/<int:id>', views.add_item_img), # renders add image form
    path('create_item_img/<int:id>', views.create_item_img), # saves image to DB

]
