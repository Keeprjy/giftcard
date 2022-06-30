from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('id', 'user_id', 'c_time', 'm_time', 'email', 'password')
#         model = models.User

# class giftcardSerializers(serializers.ModelSerializer):
#     class Meta:
#         fields = ('id', 'giftcard_id', 'user_id', 'c_time', 'm_time', 'title', 'email', 'content')
#         model = models.giftcard

 
class userSerializers(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields =  '__all__'

    # def create(self, validated_data):
    #     user = User(
    #         username=validated_data['username']
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user




class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user


class giftcardSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,)
    title = serializers.CharField(max_length=256,default = 'DEFAULT VALUE')
    content = serializers.CharField()

    class Meta:
        model = models.giftcard
        fields = ('id', 'giftcard_id', 'user_id', 'c_time', 'm_time', 'title', 'email', 'content')


    def create(self, validated_data):
        giftcard = models.giftcard.objects.create(
            giftcard_id = validated_data['giftcard_id'],
            user_id = validated_data['user_id'],
            # c_time = validated_data['c_time'],
            # m_time = validated_data['m_time'],
            title = validated_data['title'],
            email = validated_data['email'],
            content = validated_data['content'],
            # email=validated_data['models.email'],
            # title=validated_data['title'],
            # content= validated_data['content'],
        )

        
        giftcard.save()

        return models.giftcard