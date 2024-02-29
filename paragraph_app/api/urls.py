
from django.urls import path,include
#from paragraph_app.api.views import paragraph_list,paragraph_content

from  paragraph_app.api.views import ParagraphListAV,ParagraphDescriptionAV

urlpatterns = [
    path('list/', ParagraphListAV.as_view(),name='paragraph_list'),
    path('<int:pk>',ParagraphDescriptionAV.as_view(), name='paragraph_content'),
   # path('api-auth/',include('rest_framework.urls')),
]
