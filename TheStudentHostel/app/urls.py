from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('search/', views.search ,name='search')

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)