from django.contrib import admin
from django.utils.html import format_html

from network.models import NetworkObject, Product


@admin.action(description='Очистить задолженность перед поставщиком')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt_supplier=0)


@admin.register(NetworkObject)
class NetworkObjectAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name', 'type', 'level', 'email', 'country', 'city', 'supplier_link', 'debt_supplier', 'date_create')
    list_filter = ('city',)
    actions = [clear_debt]

    def supplier_link(self, obj):
        if obj.supplier:
            url = f"/admin/network/networkobject/{obj.supplier.id}/change/"  # Прописываем url ссылки на поставщика
            return format_html(f'<a href="{url}">{obj.supplier.name}</a>')
        return "-"

    supplier_link.short_description = 'Поcтавщик'


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'model', 'release_date', 'networkObject')
    list_filter = ('name', 'release_date',)
