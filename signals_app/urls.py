from django.urls import path
from . import views

urlpatterns = [
    path("sync-test/", views.test_sync_signal),
    path("transaction-test/", views.transaction_test),
]