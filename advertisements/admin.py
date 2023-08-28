from django.contrib import admin

# Register your models here.
from .models import Adv

@admin.register(Adv)#register model
class Advadmin(admin.ModelAdmin):
    list_display = ["id", "title", "auction", "price", "chd", "chu"]#Table form 
    list_filter = ["auction", "created_at", "id", "price"]#filters
    search_fields = ["title", "id"]#Search for ...
    actions = ["mark_auction_as_true", "mark_auction_as_false"]
    fieldsets = (#разделение по блокам при созданиии 
        ("Main information", {#название блока 
            "fields" : ("title", "description"),#указание что туда входит в кортеже 
            "classes": ["collapse"]#возможность сворачивания
        }),
        ("Finance", {
            "fields" : ("price", "auction"),
            "classes": ["collapse"]
        })
    )

    @admin.action(description="add auction")#! декоратор нужен для пометки что это действие
    def mark_auction_as_true(self, request, queryset):#always self, request!!!
        queryset.update(auction = True)#update field 'auction' as true

    @admin.action(description="remove auction")#description - что будет отображаться в списке action
    def mark_auction_as_false(self, request, queryset):
        queryset.update(auction = False)