"""
Tests of the retire_submissions management command.
"""
from __future__ import absolute_import

import mock
from django.core.management import call_command
from django.test import TestCase


class TestRetireSubmissions(TestCase):
    """
    Tests of the retire_submissions management command.
    """
    def test_all_queues(self):
        path = 'queue.management.commands.retire_submissions.Command.retire_submissions'
        with mock.patch(path) as mock_method:
            call_command(u'retire_submissions', force=True)
            assert mock_method.call_count == 1
