from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'remainderApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^appointments', include('remainder.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
