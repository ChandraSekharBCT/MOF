"""agriculture URL Configuration

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
from django.conf.urls import url 
from testapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),
    path('delete_product/<int:id>',views.delete_product),
  
    url(r'^$',views.home),
    url(r'^registerwithnormaluser/',views.registerwithnormaluser),
    url(r'^login/',views.login),
    url(r'^logout/',views.logout),
    url(r'^register/',views.register),
    url(r'^registerwithwholeseller/',views.registerwithwholeseller),
    url(r'^product/',views.product),
    url(r'^dashboard/',views.dashboard),
    url(r'^add_product/',views.add_product),
    url(r'^show_all_product/',views.show_all_product),
    url(r'^add_bank_details/',views.add_bank_details),
    url(r'^search/',views.search_product),
    url(r'^about/',views.about),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
