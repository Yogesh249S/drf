

from django.urls import path,include
from paragraph_app.views import paragraph_list,paragraph_content

urlpatterns = [
    path('list/', paragraph_list,name='paragraph_list'),
    path('<int:pk>', paragraph_content, name='paragraph_content'),
    #path('api/', include(api.urls)),
    #path('api-auth/',include('rest_framework.urls')),

]
