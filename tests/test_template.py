# -*- coding: utf-8 -*-
"""最小测试骨架。"""
import os
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'templates'))

from import_profile import ProfileStore  # noqa: E402
from audit_spec import fingerprint  # noqa: E402


class ProfileStoreTests(unittest.TestCase):
    def test_save_and_reuse_by_header_fingerprint(self):
        with tempfile.TemporaryDirectory() as folder:
            store = ProfileStore(folder)
            profile = {
                'schema': 'audit-import-profile', 'version': 1,
                'sheet': '流水', 'header_row': 1,
                'fingerprint': fingerprint('流水', ['日期']), 'fields': {'日期': '日期'},
            }
            store.save(profile)
            self.assertEqual(store.load('流水', ['日期'])['sheet'], '流水')
            self.assertIsNone(store.load('流水', ['金额']))


if __name__ == '__main__':
    unittest.main()
