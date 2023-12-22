from django.urls import path
import orders.views 

urlpatterns = [
      path("checkout", orders.views.checkout, name="checkout"),
      path("purchase_complete", orders.views.purchase_complete, name="purchase_complete"),
      path("summery", orders.views.order_summery, name="summery")
]   