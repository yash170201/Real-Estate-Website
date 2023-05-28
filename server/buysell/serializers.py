from rest_framework import serializers
from .models import Buysell, LegalAdvisor,Addproperty
# from drf_extra_fields.fields import Base64ImageField

class BuysellSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buysell
        # fields = ('pk', 'Username','name', 'email', 'Password','Age','Phone')
        fields= '__all__'


class LegalAdvisorSerializer(serializers.ModelSerializer):

    class Meta:
        model = LegalAdvisor
        # fields = ('pk', 'Username','name', 'email', 'Password','Age','Phone')
        fields= '__all__'


# class LegalAdvisorSerializer(serializers.ModelSerializers):
#       image=Base64ImageField() # From DRF Extra Fields
#       class Meta:
#         model = LegalAdvisor
#         fields = '__all__'
#       def create(self, validated_data):
#         image=validated_data.pop('File')
#         return LegalAdvisor.objects.create(image=image)


class AddPropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Addproperty
        # fields = ('pk', 'Username','name', 'email', 'Password','Age','Phone')
        fields= ('__all__')