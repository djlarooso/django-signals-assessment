import threading
import time

from django.http import HttpResponse
from django.db import transaction

from .models import TestModel


def test_sync_signal(request):

    print("Caller thread id:", threading.get_ident())

    print("Before saving model")

    start = time.time()

    TestModel.objects.create(name="Testing signal")

    end = time.time()

    print("After saving model")

    return HttpResponse(f"Execution time: {end - start}")
    

def transaction_test(request):

    try:
        with transaction.atomic():

            TestModel.objects.create(name="Transaction test")

            # force rollback
            raise Exception("Rolling back transaction")

    except Exception:
        pass

    return HttpResponse("Transaction rolled back")