import time
import threading

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TestModel, SignalLog


@receiver(post_save, sender=TestModel)
def test_signal(sender, instance, **kwargs):

    print("Signal started")

    print("Signal thread id:", threading.get_ident())

    time.sleep(3)

    SignalLog.objects.create(message="Signal executed")

    print("Signal finished")