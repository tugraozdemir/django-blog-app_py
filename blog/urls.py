# blog urls.py (projenizin ana urls.py dosyası)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Eğer 'index' ve 'about' görünümleri 'article' uygulamasında tanımlıysa, bu satır gerekli:
from article import views 

# Eğer 'index' ve 'about' görünümleri projenizin ana dizinindeki (blog) views.py'de ise:
# from . import views 
# VEYA
# from blog import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name = "index"),
    path('about/',views.about,name = "about"),

    path('accounts/', include('django.contrib.auth.urls')), 

    path('articles/',include("article.urls")),
    path('user/',include("user.urls")), 
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)