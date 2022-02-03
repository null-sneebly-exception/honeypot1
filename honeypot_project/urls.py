"""honeypot_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
#from honeypot_project.loginpage import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('store/', include('honeypot_project.loginpage.urls'))
    #path('', include('honeypot_project.loginpage.urls')),
    path('shop/', include('honeypot_project.shop.urls')),
    path('home/', include('honeypot_project.home.urls'))
    #since loginpage application is located within honeypot_project, and not same location as admin.py, we must include full path
]
