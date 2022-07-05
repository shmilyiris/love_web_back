"""love_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from views.index import index
from views.getinfo import InfoView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('johnson_iris/', index, name="index"),
    path('johnson_iris/album/', index, name="index"),
    path('johnson_iris/checkin/', index, name="index"),
    path('johnson_iris/404/', index, name="index"),
    path('johnson_iris/register/', index, name="index"),
    path('johnson_iris/login/', index, name="index"),
    path('johnson_iris/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('johnson_iris/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('johnson_iris/getinfo/', InfoView.as_view(), name="getinfo"),
]
