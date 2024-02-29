from rest_framework import serializers
from paragraph_app.models import Paragraph


#class QuerySerializer(serializers.ModelSerializer):
    #class Meta:
        #model=query
        #fields= "__all__"


class ParagraphSerializer(serializers.ModelSerializer):

    #custom serializer field
    #len_name=serializers.SerializerMethodField()

    #queries=QuerySerializer(many=True,read_only=True)

    class Meta:
        model=Paragraph

        fields= "__all__"
        #fields=['id','name','description'] # or exclude['active']


    #def get_len_name(self,object):
    #    return len(object.name)


    #field level validation
    def validate_name(self,value):

        if len(value)<2:
            raise serializers.ValidationError("name is too short")
        else:
            return value

    #object level validation
    def validate(self,data):
        if data['name']==data['description']:
            raise serializers.ValidationError("title and description should be different")
        else:
            return data

#class QuestionSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Question
        #fields = '__all__'

'''
class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model=query
        fields= "__all__"
'''

'''
class ParagraphSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    description=serializers.CharField()
    active=serializers.BooleanField()

    def create(self,validated_data):
        return Paragraph.objects.create(**validated_data)

    def update(self,instance,validated_data):

        #instance has old datal
        #validated_data has new data to be updated

        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.active=validated_data.get('active',instance.active)
        instance.save()
        return instance

    #field level validation

    def validate_name(self,value):

        if len(value)<2:
            raise serializers.ValidationError("name is too short")
        else:
            return value

    #object level validation
    def validate(self,data):
        if data['name']==data['description']:
            raise serializers.ValidationError("title and description should be different")
        else:
            return data

'''
