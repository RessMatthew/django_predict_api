from django.contrib import admin
from django.urls import path

from predict_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/alarm/', views.get), #get为view.py中的函数名
 ]