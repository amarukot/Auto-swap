from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.seller_list),
    path('seller/', views.seller_list, name = 'seller_list'),
    path('seller/<int:id>', views.seller_detail, name = 'seller_detail'),
    path('seller/new', views.seller_create, name = 'seller_create'),
    path('seller/<int:id>/edit', views.seller_update, name = 'seller_update'),
    path('seller/<int:id>/delete', views.seller_delete, name = 'seller_delete'),
    path('car/', views.car_list, name = 'car_list'),
    path('car/<int:id>', views.car_detail, name = 'car_detail'),
    path('car/new', views.car_create, name = 'car_create'),
    path('car/<int:id>/edit', views.car_update, name = 'car_edit'),
    path('car/<int:id>/delete', views.car_delete, name = 'car_delete'),
    # path('upload/', views.upload_pic, name = 'upload_pic'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)