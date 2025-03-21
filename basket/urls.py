from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart_view'),  # Отображение корзины
    path('update_cart/<int:product_id>/<int:quantity>/', views.UpdateCartView.as_view(), name='update_cart'),  # Обновление количества товара в корзине
    path('remove_from_cart/<int:product_id>/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),  # Удаление товара из корзины
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),  # Оформление заказа
]
