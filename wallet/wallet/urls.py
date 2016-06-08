"""wallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from auths.views import IndexView, Registration, Authentication

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # We won't be able to capture /admin/ urls otherwise
    url(r'^$', IndexView.as_view(), name="home"),
    url(r'^registration/', Registration.as_view(), name="sign up"),
    url(r'^authentication/', Authentication.as_view(), name="sign in"),
    url(r'mywallet/', include('mywallet.urls')),
]
