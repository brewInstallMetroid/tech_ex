from django.urls import path
from . import views

urlpatterns = [path("credit-memo/",
                    views.credit_memo,
                    name="credit_memo",),
               path("search-customer/",
                    views.search_customer,
                    name="search_customer",),
               path("search-item/",
                    views.search_item,
                    name="search_item",),
               ]
