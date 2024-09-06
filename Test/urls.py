"""
URL configuration for Test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from student_info.views import *
from recipe.views import *
from django.conf import settings
from django.conf.urls.static import static
# from coustomUser.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("recipe/",recipe,name="recipes"), 
    path('student/',student,name="home"),
    path('recipe-disply/',disply_recipe,name="disply_recipe"),
    path('delete-recipe/<id>/', recipe_delete, name="delete_recipe"),
    path('update-recipe/<id>/', update_recipe, name="update_recipe"),
    path('',login_view,name="login_view"),
    path('signup_view/',signup_view,name="signup_view"),
    path('logout_view/',logout_view,name="logout_view"),
    
    # path('update-recipe/<id>/', update_recipe, name="update_recipe"),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)