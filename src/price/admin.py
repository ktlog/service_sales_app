from django.contrib import admin
from price.models import PriceCard, PriceTable


class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'pc_value', 'pc_description')
    list_display_links = ('pc_value', 'pc_description')


class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'pt_title', 'pt_old_price', 'pt_new_price')
    list_display_links = ('pt_title', )


admin.site.register(PriceCard, CardAdmin)
admin.site.register(PriceTable, TableAdmin)
