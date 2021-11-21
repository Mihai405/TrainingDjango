from rest_framework import serializers
from .models import Friend

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model   =   Friend
        fields  =   ['id','first_name','last_name','phone_number']
        read_only_fields = ['user']

    def validate_phone_number(self,value):
        if len(value) < 10 :
            raise serializers.ValidationError("The phone number is not long enough")
        if value[0]!='0':
            raise serializers.ValidationError("The phone number should start with 0")
        if value.isdigit()==False:
            raise serializers.ValidationError("The phone number should contain only digits")
        return value