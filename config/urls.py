"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.friends.urls import routes as friends_routes
from apps.users.urls import routes as users_routes
from apps.friends.views import APIFriendsView,APIUpdateFriendView
from apps.users.views import LogInView,LogOutView
from rest_framework.routers import DefaultRouter
from django.urls import include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Friends API",
      default_version='v1',
      description="You should use Login View if you are Unauthenticated,in order to access the Views",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

api_routes=[]
api_routes.append(friends_routes)
api_routes.append(users_routes)

router  =   DefaultRouter()

for routes in api_routes:
    for r in routes:
        router.register(r[0],r[1])

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('login/',LogInView.as_view(),name='login'),
    path('logout/',LogOutView.as_view(),name='logout'),
    path('friends/',APIFriendsView.as_view(),name='friends'),
    path('friend/<int:pk>/',APIUpdateFriendView.as_view(),name='update_friend'),
]