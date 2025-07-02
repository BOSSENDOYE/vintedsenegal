from rest_framework import serializers
from .models import Transaction, Commission

class CommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commission
        fields = ['id', 'transaction', 'percentage', 'amount']

class TransactionSerializer(serializers.ModelSerializer):
    commissions = CommissionSerializer(many=True, read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'user', 'amount', 'status', 'created_at', 'commissions']
