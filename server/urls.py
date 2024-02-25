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
    path('phone', reg.RegistrationPhoneStepView.as_view()),
    path('sms', reg.RegistrationSMSStepView.as_view()),
    path('private', reg.RegistrationPasswordStep.as_view()),
    path('finish', reg.CreateUserView.as_view()),
]

items_patterns = [
    path('list', items.ItemsListView.as_view()),
    path('item', items.ItemView.as_view()),
    path('like', like.LikeView.as_view()),
    path('category', items.CategoryView.as_view()),
    path('subcategory', items.SubCategoryView.as_view())
]

location_patterns = [
    path('country', locs.CountryView.as_view()),
    path('region', locs.RegionView.as_view()),
    path('district', locs.DistrictView.as_view())
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', include(registratio_patterns)),
    path('authorize', auth.LoginView.as_view()),
    path('logout', auth.LogoutView.as_view()),
    path('items/', include(items_patterns)),
    path('location/', include(location_patterns)),
    path("accounts/", include(urls)),
    path("o/", include('oauth2_provider.urls', namespace='oauth2_provider')),
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
