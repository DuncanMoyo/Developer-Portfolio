from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user.views import index
from posts.views import search, blog, post_create, post_update, post_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('blog/<id>/', blog, name='post-detail'),
    path('create/', post_create, name='post-create'),
    path('blog/<id>/update/', post_update, name='post-update'),
    path('blog/<id>/delete/', post_delete, name='post-delete'),
    path('tinymce/', include('tinymce.urls')),
    path('search/', search, name='search')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

