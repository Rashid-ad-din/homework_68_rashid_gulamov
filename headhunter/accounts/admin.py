from django.contrib import admin

from accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'usertype', 'phone')
    list_filter = ('username', 'email', 'usertype', 'phone')
    search_fields = ('username', 'email', 'usertype')
    readonly_fields = ('id', 'date_joined')

    fieldsets = (
        ('', {
            'fields': ('username', 'email', 'usertype', 'phone')
        }),
    )


admin.site.register(Account, AccountAdmin)
