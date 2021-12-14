from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from . import settings


schema_view = get_schema_view(
    openapi.Info(

        title="Authentication API",
        default_version='v1',
        description='SomeDescription'
    ),
    public=True
)

urlpatterns = [
    path('', schema_view.with_ui()),
    path('admin/', admin.site.urls),
    path('post/', include('applications.posts.urls')),
    path('account/', include('applications.account.urls')),
    path('comment/', include('applications.comment.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
