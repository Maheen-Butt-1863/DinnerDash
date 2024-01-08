from django.urls import path

from .views import (
    AdminOrderDetailsView,
    CartPageView,
    CategoryUpdate,
    CustomLoginView,
    CustomLogoutView,
    HomePageView,
    ItemUpdateView,
    OrderDetailsView,
    SignUpView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("home/", HomePageView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("cart/", CartPageView.as_view(), name="cart"),
    path("order_details/", OrderDetailsView.as_view(), name="order_details"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("item/", ItemUpdateView.as_view(), name="item"),
    path("category/", CategoryUpdate.as_view(), name="category"),
    path(
        "admin_order_details/",
        AdminOrderDetailsView.as_view(),
        name="admin_order_details",
    ),
]