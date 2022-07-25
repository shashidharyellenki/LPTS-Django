
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students_Directory_page.urls')),
    path('', include('NewUserRegistrationForm.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
