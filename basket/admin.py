from django.contrib import admin
from .import models


admin.site.register(models.Cart)
admin.site.register(models.CartItem)  # Регистрация CartItem в админке
admin.site.register(models.Order)