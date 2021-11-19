from auth_app.models.account import Account
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id', 'user','balance', 'lastChangeDate', 'isActive']