from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include

from project import settings

urlpatterns = static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += [
    url(r'', include('apps.main.urls')),
]
