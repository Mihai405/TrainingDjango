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
from apps.friends.views import APIListFriendsView,APIAddFriendView,APIUpdateFriendView,APIDeleteFriendView
from apps.users.views import LogInView
from rest_framework.routers import DefaultRouter
from django.urls import include

api_routes=[]
api_routes.append(friends_routes)
api_routes.append(users_routes)

router  =   DefaultRouter()

for routes in api_routes:
    for r in routes:
        router.register(r[0],r[1])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('login/',LogInView.as_view()),
    path('friends/',APIListFriendsView.as_view()),
    path('add-friends/',APIAddFriendView.as_view()),
    path('friend/<int:pk>/',APIUpdateFriendView.as_view()),
    path('delete-friends/<int:pk>/',APIDeleteFriendView.as_view()),
]
