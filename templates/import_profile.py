# -*- coding: utf-8 -*-
"""通用导入映射存取示例，供新程序复制。"""
import json
import os

from audit_spec import fingerprint, validate_import_profile


class ProfileStore:
    def __init__(self, root):
        self.root = root
        os.makedirs(root, exist_ok=True)

    def _path(self, key):
        return os.path.join(self.root, key + '.json')

    def save(self, profile):
        errors = validate_import_profile(profile)
        if errors:
            raise ValueError('；'.join(errors))
        path = self._path(profile['fingerprint'])
        with open(path, 'w', encoding='utf-8') as handle:
            json.dump(profile, handle, ensure_ascii=False, indent=2)
        return path

    def load(self, sheet, headers):
        key = fingerprint(sheet, headers)
        path = self._path(key)
        if not os.path.isfile(path):
            return None
        with open(path, 'r', encoding='utf-8') as handle:
            profile = json.load(handle)
        return None if validate_import_profile(profile) else profile
