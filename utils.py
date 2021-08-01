"""
This module provides utility functions
"""
import error

DEFAULT_CARDS_PER_PAGE = 12


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

    data = request.get_json(force=True)
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