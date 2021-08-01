"""
This module provides backend resources
"""

import time
import math
import random
from utils import DEFAULT_CARDS_PER_PAGE
from model import Catalog, Service, Version


class Resource:
    def __init__(self):
        self.catalog = Catalog()

    def get_services(self, query=None, page_length=DEFAULT_CARDS_PER_PAGE, page=0):
        """
        Retrieve services stored in data modeling/storage

        :param query:
        :param page_length:
        :param page:
        :return: a list of services, max_page
        """

        if not query:
            return self.catalog.services[page*page_length:(page+1)*page_length], max(int(math.ceil(len(self.catalog.services) / float(page_length))) - 1, 0)

        filtered_services = [s for s in self.catalog.services if query.lower() in s.name.lower() or query.lower() in s.description.lower()]

        return filtered_services[page*page_length:(page+1)*page_length], max(int(math.ceil(len(filtered_services) / float(page_length))) - 1, 0)

    def get_service(self, service_id):
        """
        Retrieve a single service stored in data modeling/storage given service_id

        :param service_id:
        :return: a service or None
        """

        for s in self.catalog.services:
            print(s.service_id)
            if s.service_id == service_id:
                return s
        return None

    def add_service(self, name, description):
        """
        Add user input service into data modeling/storage

        :param name:
        :param description:
        :return: service id
        """
        service = Service()
        service.name = name
        service.description = description
        service.created_ts = long(time.time())
        service.service_id = long(time.time()) + random.randint(0, 100)  # Use timestamp + a random number to generate ID

        version = Version()
        version.version_id = long(time.time()) + random.randint(0, 100)  # Use timestamp + a random number to generate ID
        version.service_id = service.service_id
        service.versions.insert(0, version)

        # This is to ensure newly added service will be in the front of the list
        self.catalog.services.insert(0, service)

        return service.service_id
