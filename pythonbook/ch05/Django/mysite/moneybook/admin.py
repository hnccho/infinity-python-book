from django.contrib import admin
from moneybook.models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'value')
    
admin.site.register(Transaction, TransactionAdmin)
