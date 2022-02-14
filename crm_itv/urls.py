"""crm_itv URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('deal_fct_nonfct.urls', namespace = 'deal_fct_nonfct')),
    path('',include('events_afp.urls', namespace = 'events_afp')),
    path('',include('accounts.urls',namespace='accounts')),
    path('',include('profiles.urls')),
    path('',include('agency.urls',namespace='agency')),
    path('',include('customer.urls',namespace='customer')),
    path('nfct/',include('nfct.urls',namespace='nfct')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)