from django.contrib import admin
from .models import *


class walletAdmin(admin.ModelAdmin):
    list_display = ('user', 'credict_ballance', 'Currency', 'Billing_Address')
    
class transaction_historyAdmin(admin.ModelAdmin):
    list_display = ('Sender','user', 'amount',)


admin.site.register(profile)
admin.site.register(users_wallet,walletAdmin)
admin.site.register(transaction,transaction_historyAdmin)

