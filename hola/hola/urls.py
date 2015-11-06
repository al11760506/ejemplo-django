from django.conf.urls import *
from django.contrib import admin
from hola.views import current_datetime
from hola.views import  hours_ahead
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hola.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})$', hours_ahead),
    
)
