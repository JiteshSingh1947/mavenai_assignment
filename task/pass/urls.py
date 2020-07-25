from django.urls import path ,include
from .import views	

from rest_framework import routers 

router = routers.DefaultRouter()
router.register('', views.proView)

    

urlpatterns=[
	path('',views.register,name='xyz'),
	path('dashboard/',views.detail,name='abc'),
	path('api/', include(router.urls)),
	 ]