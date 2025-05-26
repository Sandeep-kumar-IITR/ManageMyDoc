# """
# URL configuration for djangoback project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """

# from django.contrib import admin
# from django.urls import path
# from myapp.views import Listdoc, Detaildoc , CreateDoc , DeleteDoc

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
    
# )




# from myapp.views import RegisterView
# from myapp.views import LoginView
# from myapp.views import DashboardView
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path('api/api/auth/register/', RegisterView.as_view(), name='register'),
#     path('api/api/auth/login/', LoginView.as_view(), name='login'),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('api/dashboard/', DashboardView.as_view(), name='dashboard'),



#     path('ap/', Listdoc.as_view(), name='listdoc'),


#     path('ap/<int:pk>/', Detaildoc.as_view(), name='detaildoc'),
    
#     path('ap/create/', CreateDoc.as_view(), name='createdoc'),
    
#     path('ap/delete/<int:pk>/', DeleteDoc.as_view(), name='deletedoc'),



# ]
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from myapp.views import Listdoc, Detaildoc, CreateDoc, DeleteDoc
from myapp.views import RegisterView, LoginView, DashboardView


from myapp.views import CreateChatMessage,Listuser_message



from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/api/auth/login/', LoginView.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/dashboard/', DashboardView.as_view(), name='dashboard'),

    path('ap/', Listdoc.as_view(), name='listdoc'),
    path('ap/<int:pk>/', Detaildoc.as_view(), name='detaildoc'),
    path('ap/create/', CreateDoc.as_view(), name='createdoc'),
    path('ap/delete/<int:pk>/', DeleteDoc.as_view(), name='deletedoc'),
    path('chatlist/',Listuser_message.as_view(), name='chatlist'),
    path('chat/', CreateChatMessage.as_view(), name='chat'),
]

# Add this block to serve media files during development
# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
