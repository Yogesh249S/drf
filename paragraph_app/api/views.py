#from rest_framework.decorators import api_view
from paragraph_app.models import Paragraph

from paragraph_app.api.serializers import ParagraphSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
'''
#function based views ---using decorators
#----------------------------------------------------------------------
@api_view(['GET','POST'])
def paragraph_list(request):

    if request.method =='GET':
        paragraph=Paragraph.objects.all()
        serializer=ParagraphSerializer(paragraph,many=True)
    #many-True is done because there are multiple objcets serializer visit many elements
        return Response(serializer.data)

    if request.method =='POST':
        #get data from user
        serializer=ParagraphSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)




@api_view(['GET','PUT','DELETE'])
def paragraph_content(request,pk):

    if request.method =='GET':
        try:
            paragraph=Paragraph.objects.get(pk=pk)
        except Paragraph.DoesNotExist:
            return Response({'Error':'Paragraph not found'},status=status.HTTP_404_NOT_FOUND)


        serializer=ParagraphSerializer(paragraph)
        return Response(serializer.data)

    if request.method =='PUT':
        paragraph=Paragraph.objects.get(pk=pk)
        serializer=ParagraphSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    if request.method =='DELETE':
        paragraph=Paragraph.objects.get(pk=pk)
        paragraph.delete()

        #send response
        return Response(status=status. HTTP_204_NO_CONTENT)

'''

#class based views
#-------------------------------------------------------------------------------------------------
class ParagraphListAV(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        paragraph=Paragraph.objects.all()
        serializer=ParagraphSerializer(paragraph,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ParagraphSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ParagraphDescriptionAV(APIView):

    def get(self,request,pk):

        try:
            paragraph=Paragraph.objects.get(pk=pk)
        except Paragraph.DoesNotExist:
            return Response({'Error':'Paragraph not found'},status=status.HTTP_404_NOT_FOUND)

        serializer=ParagraphSerializer(paragraph)
        return Response(serializer.data)


    def put(self,request,pk):
        paragraph=Paragraph.objects.get(pk=pk)
        serializer=ParagraphSerializer(paragraph,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        paragraph=Paragraph.objects.get(pk=pk)
        paragraph.delete()

        #send response
        return Response(status=status. HTTP_204_NO_CONTENT)


#class QuestionsAPIView(generics.ListCreateAPIView):
    #search_fields = ['question_text']
    #filter_backends = (filters.SearchFilter,)
    #queryset = Question.objects.all()
    #serializer_class = QuestionSerializer



#class QueryAV(generics.ListCreateAPIView):
    #'''
    #def get(self,request):
        #serializer=ParagraphSerializer(data=request.data)
    #'''
    #search_fields = ['question_text']
    #filter_backends = (filters.SearchFilter,)
    #queryset = query.objects.all()
    #serializer_class = QuerySerializer


