from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls'))
]

# ⚠️ Apenas para desenvolvimento! 
# Em produção, use Nginx/Apache ou serviços como S3/GCP para servir arquivos.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Uploads de usuários
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # CSS, JS, imagens
