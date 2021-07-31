"""
This module serves as database models
"""


class Catalog:
    def __init__(self):
        self.services = []


class Service:
    def __init__(self):
        self.service_id = ""
        self.name = ""
        self.description = ""
        self.created_ts = 0
        self.user_id = 0
        self.versions = []


class Version:
    def __init__(self):
        self.version_id = ""
        self.service_id = ""
        self.name = ""


