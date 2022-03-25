from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls', namespace='home')),
    path('category/', include('apps.category.urls', namespace='category')),
    path('content-type/', include('apps.course_content.urls', namespace='content_type')),
    path('platform/', include('apps.course_platform.urls', namespace='platform')),
    path('subscription/', include('apps.subscription.urls', namespace='subscription')),
    path('course/', include('apps.course.urls', namespace='course')),
    path('pricing/', include('apps.payment.urls', namespace='payment')),
    path('instructor/', include('apps.instructor.urls', namespace='instructor')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
