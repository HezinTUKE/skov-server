"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import urls
from registration import views as reg
from authentication import views as auth
from items_list import views as items
from locations import views as locs
from like_post import views as like

registratio_patterns = [
    path('phone', reg.get_phone),
    path('sms', reg.check_sms),
    path('private', reg.get_user_private),
    path('finish', reg.get_user_data),
]

items_patterns = [
    path('list', items.get_list),
    path('categorys', items.get_categorys),
    path('item', items.get_item),
    path('create', items.create_item),
    path('like', like.post_like)
]

location_patterns = [
    path('country', locs.get_country),
    path('region', locs.get_regions),
    path('district', locs.get_districts)
]

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('registration/', include(registratio_patterns)),
    path('login', auth.auth_login),
    path('logout', auth.auth_logout),
    path('items/', include(items_patterns)),
    path('location/', include(location_patterns)),
    path("accounts/", include(urls)),
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
