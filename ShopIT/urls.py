
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

admin.site.site_header = "StyleIT Admin"
admin.site.site_title = "Wellcome To StyleIT Portal"
admin.site.index_title = "Welcome to SuperAdmin Panel!"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('cart', include('cart.urls'))
    
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  