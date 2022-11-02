
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('', include('feeds.urls')),
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('routes/', include('routes.urls')),
    path('vetoffice/', include('vetoffice.urls')),

    

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
