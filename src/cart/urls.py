from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('cart/', views.CartDetailView.as_view(), name='view-cart'),
    path('edititem/', views.CartAddDeleteView.as_view(), name='edit-item'),
    path('createorder/', views.CreateOrder.as_view(), name='create-order'),
    path('successorder/', views.success_order, name='success-order'),
    path('adminorder/', views.OrderListView.as_view(), name='admin-order'),
    path('adminordersedit/<int:pk>', views.OrderUpdateView.as_view(), name='admin_orders_update'),
    path('adminordersdelete/<int:pk>', views.OrderDeleteView.as_view(), name='admin_orders_delete'),
    path('open/', views.open_orders, name='open-order')
]