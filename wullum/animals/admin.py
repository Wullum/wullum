from django.contrib import admin

from .models import Animals, Weights, Comments, Fat, FoodPurchases, MiscPurchases, Eggs

# Register your models here.
admin.site.register(Animals)
admin.site.register(Weights)
admin.site.register(Comments)
admin.site.register(Fat)
admin.site.register(FoodPurchases)
admin.site.register(MiscPurchases)
admin.site.register(Eggs)
