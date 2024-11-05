from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

UserModel = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)
    phone_number = serializers.CharField(
        max_length=15,
        validators=[UniqueValidator(queryset=UserModel.objects.all(), message="Phone number already exists")]
    )
    password = serializers.CharField(max_length=128, write_only=True, required=True)

    class Meta:
        model = UserModel
        fields = ['username', 'phone_number', 'password', 'confirm_password']

    def validate(self, attrs):
        password = attrs.get('password').strip()
        confirm_password = attrs.get('confirm_password').strip()
        phone_number = attrs.get('phone_number').strip()

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match!")

        if not phone_number.startswith('+998'):
            raise serializers.ValidationError("Phone number must start with +998")

        if not phone_number[4:].isdigit():
            raise serializers.ValidationError("Phone number must be contain only digits after the country code!")

        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = UserModel.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=15, required=True)
    password = serializers.CharField(min_length=8, write_only=True, required=True)
