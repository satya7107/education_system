"""
URL configuration for education project.

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
from django.urls import path,include
from mysite import views as anoviews
from todo_app import views as tviews
from todo_register import views as rviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index1',anoviews.index1),

    # for practice1 use
    path('index',anoviews.index,name='index'),
    path('dstudent/',include('dstudent.urls')),
    path('duser/',include('duser.urls')),
    # for practice2 use
    path('todo_app',tviews.todo_app, name='todo_app'),
    path('addtask/',include('addtask.urls')),
    # for practice3 use
    path('dsignup',rviews.dsignup),


    path('header',anoviews.header),
    
    path('footer',anoviews.footer),

    path('base',anoviews.base),

    path('',anoviews.homepage,name='homepage'),

    path('features',anoviews.features),


    #experties all data
    path('experties',anoviews.experties,name='experties'),
    path('dexperties/',include('dexperties.urls')),
    path('dceo/',include('dceo.urls')),
    path('dchanc/',include('dchanc.urls')),
    path('dprinc/',include('dprinc.urls')),
    path('dvprinc/',include('dvprinc.urls')),
    path('dfact/',include('dfact.urls')),
    


    path('contactus',anoviews.contactus),
    
    path('gallery', anoviews.gallery),
    
    path('login',anoviews .login),

    path('signup',anoviews.signup),

    #harry course
    path('mymain/',anoviews.mymain,name='mymain'),
    path('analyze/',anoviews.analyze,name='analyze'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
