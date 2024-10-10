from django.contrib import admin
from django.urls import path
from myproject import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('table/', views.table,name='table'),
    path('base/', views.base,name='base'),
    path('home/', views.home,name='home'),
    path('', views.loginpage,name='loginpage'),
    path('logoutpage/', views.logoutpage,name='logoutpage'),
    path('registerpage/', views.registerpage,name='registerpage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
