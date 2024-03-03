
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('meals/',include('app_meal.urls')),
    path('',views.home)
]
