
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index),
    path('login_reg', views.login_reg), # render registration template
    path('process_reg', views.process_reg), # adds user to DB
    path('login', views.login), # log in, gets user from DB then redirect to sucsess
    path('sucsess', views.sucsess), # to render appropriate template for artist/customer
    path('add_item', views.add_item), # renders add item page for artist
    path('create_art', views.create_art), # adds artwork to DB
    
    path('artwork_info/<artwork_id>', views.artwork_info), # render a one artwork details page
    path('buy_artwork/<artwork_id>', views.buy_artwork),
    path('add_review/<artwork_id>', views.add_review),
    path('show_artist_profile/<artist_id>', views.show_artist_profile),
    path('logout', views.logout),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
