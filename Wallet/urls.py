from django.conf.urls import url
from .views import login, RemoveTransactionView, AddTransactionView


urlpatterns = [
    url(r'^v1/addMoney/(?P<wallet_id>[a-zA-Z]+)/$', AddTransactionView.as_view()),
    url(r'^v1/withdrawMoney/(?P<wallet_id>[a-zA-Z]+)/$', RemoveTransactionView.as_view()),
    url(r'^v1/login/$', login),
]
