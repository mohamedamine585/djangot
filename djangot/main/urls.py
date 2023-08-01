from django.urls import path
from main import views
urlpatterns = [
    path("get_apps/",views.apps_list),
    path("post_offer/",views.post_offer),
    path("get_offers/",views.offers_list),
    path("post_app/",views.post_app),
    path("delete_app/<int:idapp>/",views.delete_app)
]