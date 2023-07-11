from django.db import models
from django.contrib.auth import get_user_model
from reference.models import Title


# Create your models here.
User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        User, 
        verbose_name='Customer',
        on_delete=models.PROTECT,
        related_name='carts',
        null=True,
        blank=True
    )

    @property
    def total_price(self):
        total_price = 0
        for item_in_cart in self.items.all():
            total_price += item_in_cart.price
        return total_price

class ItemsInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name='Cart',
        on_delete=models.CASCADE,
        related_name='items'
    )

    item = models.ForeignKey(
        Title,
        verbose_name='Book',
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        verbose_name='Quantity',
        default=1
    )

    price = models.DecimalField(
        verbose_name='Price',
        max_digits=6,
        decimal_places=2
    )

    created = models.DateTimeField(
        verbose_name='Created',
        auto_now_add=True,
        auto_now=False
    )

    updated = models.DateTimeField(
        verbose_name='Updated',
        auto_now_add=False,
        auto_now=True
    )

    def __str__(self) -> str:
        return f'{self.item.book_title} x {self.quantity}'
    
class Status(models.Model):
    status = models.CharField(
        verbose_name='Status',
        max_length=256
    )

    def __str__(self):
        return self.status

class Order(models.Model):
    user = models.ForeignKey(
        User,
        default=1,
        on_delete=models.CASCADE
    )

    phone = models.CharField(
        verbose_name='Phone',
        max_length=256,
        default='+375',
        null=False,
        blank=False
    )
    
    address = models.TextField(
        verbose_name='Delivery address'
    )

    item = models.TextField(
        verbose_name='Item'
    )

    status = models.ForeignKey(
        Status,
        verbose_name='Status',
        on_delete=models.PROTECT
    )

    payment_method = models.CharField(
        verbose_name='Payment',
        max_length=256,
        null=False,
        blank=False
    )

    cart = models.OneToOneField(
        Cart,
        verbose_name='Cart',
        on_delete=models.PROTECT
    )

    created = models.DateTimeField(
        verbose_name='Created',
        auto_now_add=True,
        auto_now=False
    )

    updated = models.DateTimeField(
        verbose_name='Updated',
        auto_now_add=False,
        auto_now=True
    )

    def get_absolute_url(self):
        return '/success'
    
    def get_search_url(self):
        return f'/cart/adminordersedit/{self.pk}'