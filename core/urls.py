from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    #Añadiendo las urls del  blog en el core principal
    path('blog/', include('blog.urls', namespace='blog')),
]

# Ruta para archivos de medios
if settings.DEBUG:  # Solo en modo desarrollo
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)