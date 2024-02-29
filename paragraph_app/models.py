from django.db import models

# Create your models here.
'''
class Paragraph(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    active = models.BooleanField(default=True)
    #date_of_birth=models.DateField()
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name
'''

class Paragraph(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000,default='empty')
    active = models.BooleanField(default=True)
    email = models.EmailField(max_length=50,default='new@gmailcom')

    #dob = models.DateField(format=api_settings.DATE_FORMAT, input_formats=None)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    #creator = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


#class Question(models.Model):
    #question_text = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published', null=True)
    #author = models.CharField(max_length=200, null=True)

    #def __str__(self):
        #return self.question_text


#class Choice(models.Model):
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #choice_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)

    #def __str__(self):
        #return self.choice_text
'''
class query(models.Model):
    search=models.CharField(max_length=50)
    #description=models.CharField(max_length=200,null=True)
    paragraph=models.ForeignKey(Paragraph,on_delete=models.CASCADE,related_name='queries')

    def __str__(self):
        return str(self.search)
'''
