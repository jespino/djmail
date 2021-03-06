# -*- coding: utf-8 -*-

from __future__ import absolute_import

from django.conf import settings
from djmail.backends import base
from djmail import core
from djmail import tasks


class EmailBackend(base.BaseEmailBackend):
    def _send_messages(self, email_messages):
        if len(email_messages) == 0:
            return 0

        return tasks.send_messages.delay(email_messages)
