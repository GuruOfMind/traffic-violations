from django.conf import settings
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.contrib import admin

admin.site.site_header = 'E-PTV Admin Panel'
admin.site.site_title = 'E-PTV Admin Panel'
urlpatterns = [
    path('', include('frontend.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
