
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register), # render registration template
    path('process_reg', views.process_reg), # adds user to DB
    path('login_form', views.login_form), # renders log in form
    path('login', views.login), # log in, gets user from DB then redirect to sucsess
    path('sucsess', views.sucsess), # to render appropriate template for artist/customer
    path('add_item', views.add_item), # renders add item page for artist
    path('create_art', views.create_art), # adds artwork to DB
    path('add_item_img/<int:artwork_id>', views.add_item_img), #renders upload img form
    path('create_item_img/<int:artwork_id>', views.create_item_img), #saves img to DB
    path('edit_item/<int:artwork_id>', views.edit_item),
    path('update_artwork/<int:artwork_id>', views.update_artwork),
    path('delete_artwork/<int:artwork_id>', views.delete_artwork),
    
    path('checkout', views.check_out_page),
    path('checkout/<int:artwork_id>/<int:customer_id>', views.check_out),
    path('art_gallery', views.art_gallery),
    path('payment/<int:artwork_id>', views.payment),
    path('payment_success/<int:artwork_id>', views.payment_success),

    path('artwork_info/<artwork_id>', views.artwork_info), # render a one artwork details page
    path('buy_artwork/<artwork_id>', views.buy_artwork),
    path('add_review/<artwork_id>', views.add_review),
    path('show_artist_profile/<artist_id>', views.show_artist_profile),
    path('edit_artist_bio/<int:artist_id>', views.edit_artist_bio),
    path('update_artist_bio/<int:artist_id>', views.update_artist_bio),
    
    path('all_artists', views.all_artists),
    path('logout', views.logout),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
