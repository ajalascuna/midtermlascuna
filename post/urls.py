from django.urls import path
from . import views
app_name = 'post'

urlpatterns = [
    path('', views.index, name='index'),
    #path('help/', views.help, name='help'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/update', views.update, name='update')
]
