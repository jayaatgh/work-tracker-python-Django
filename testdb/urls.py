from django.urls import path
from . import views
urlpatterns = [
    path('',views.registerdata),
    path('userlog/',views.userlog),
    path('adminlog/',views.adminlog),
    path('pending/',views.pending),
    path('approved/', views.approved),
    path('approve/<int:id>/',views.approve),
    path('edit/<int:id>/',views.edit),
    path('delete/<int:id>/',views.delete),
    path('upload/',views.upload),
    path('viewimage/',views.img_view),

]