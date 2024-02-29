
from django.shortcuts import render
from paragraph_app.models import Paragraph
from django.http import JsonResponse
# Create your views here.

:
    paragraph=Paragraph.objects.all()
    data={'paragraph':list(paragraph.values())
    }



    return JsonResponse(data)

def paragraph_content(request,pk):
    paragraph=Paragraph.objects.get(pk=pk)

    data={
        'name':paragraph.name,
        'description':paragraph.description,
        'active':paragraph.active
        }
    return JsonResponse(data)

