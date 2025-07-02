from django.contrib import admin
from .models import Transaction, Commission

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'status', 'created_at')
    search_fields = ('user__username', 'status')

@admin.register(Commission)
class CommissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'transaction', 'percentage', 'amount')
