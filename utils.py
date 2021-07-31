import time
import math
import random
import error
from model import Catalog, Service, Version

DEFAULT_CARDS_PER_PAGE = 12
catalog = Catalog()


def get_services(query, page_length, page):
    """
    Retrieve services stored in data modeling/storage

    :param query:
    :param page_length:
    :param page:
    :return: a list of services
    """

    if not query:
        return catalog.services[page*page_length:(page+1)*page_length], int(math.ceil(len(catalog.services) / page_length))

    filtered_services = [s for s in catalog.services if query.lower() in s.name.lower() or query.lower() in s.description.lower()]

    return filtered_services[page*page_length:(page+1)*page_length], int(math.ceil(len(filtered_services) / page_length))


def get_service(service_id):
    """
    Retrieve a single service stored in data modeling/storage given service_id

    :param servuce_id:
    :return: a service or None
    """

    for s in catalog.services:
        print(s.service_id)
        if s.service_id == service_id:
            return s
    return None


def add_service(name, description):
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
    catalog.services.insert(0, service)

    return service.service_id


def validate_get_services_request(request):
    """
    Validate the get_services requests and return 3 parameters

    :param request: A{I request
    :return: query, page_length, page
    """
    user_id = request.headers.get("user_id")
    validate_user_permission(user_id)

    query = request.args.get("query") if request.args.get("query") else ""
    page_length = int(request.args.get("page_length")) if request.args.get("page_length") else DEFAULT_CARDS_PER_PAGE
    page = int(request.args.get("page")) if request.args.get("page") else 0

    return query, page_length, page


def validate_add_service_request(request):
    """
    Validate the add_service requests and return 2 parameters

    :param request: API request
    :return: name, description
    """
    user_id = request.headers.get("user_id")
    validate_user_permission(user_id)

    data = request.get_json()
    name = data.get("name")
    description = data.get("description") if data.get("description") else ""

    validate_name_and_description(name, description)

    return name, description


def validate_user_permission(user_id):
    """
    User authentication/authorization

    :param user_id:
    :return:
    """
    # TODO: IAM logic
    pass


def validate_name_and_description(name, description):
    """
    Input validation

    :param name:
    :param description:
    :return:
    """
    if not name:
        raise error.InvalidInputError()

    # TODO: Validate if the language is appropriate
    # TODO: Validate if the string has JavaScript injections
    pass

# add_service("test3", "hello3")
# time.sleep(1)
# add_service("test2", "hello2")
# time.sleep(1)
# add_service("test1", "hello1")
# time.sleep(1)
# add_service("test4", "hello4")
# time.sleep(1)
# add_service("test5", "hello5")