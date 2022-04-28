from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password')

    def create(self, validated_data):
        # setting the user password in the following way
        # because the password must be hashed
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    # called on return
    # removing password from response
    def to_representation(self, instance):
        result = super().to_representation(instance)
        result.pop('password')
        return result
