from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from sale import views



urlpatterns = [
    url(r'^$',views.login_redirect,name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^categry/', include('category.urls')),
    url(r'^tac/', include('tac.urls')),
    url(r'^computer/', include('computer.urls')),
    url(r'^automobiles/', include('automobiles.urls')),
    url(r'^mobiles/', include('mobiles.urls')),
    url(r'^electronics/', include('electronics.urls')),
    url(r'^apparels/', include('apparels.urls')),
    ]


if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
