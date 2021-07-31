from flask import Flask, json, request, abort
import utils
import error
from representation import GetServicesResponse, GetServiceResponse, AddServiceResponse

api = Flask(__name__)


@api.route('/services', methods=['GET'])
def get_services():
    query, page_length, page = utils.validate_get_services_request(request)

    services, max_page = utils.get_services(query=query, page_length=page_length, page=page)

    return json.dumps(GetServicesResponse.get_response(services, page, max_page))


@api.route('/service/<service_id>', methods=['GET'])
def get_service(service_id):

    service = utils.get_service(int(service_id))

    return json.dumps(GetServiceResponse.get_response(service))


@api.route('/add_service', methods=['POST'])
def add_service():
    try:
        name, description = utils.validate_add_service_request(request)

        service_id = utils.add_service(name, description)
        return json.dumps(AddServiceResponse.get_response(service_id))
    except error.InvalidInputError:
        abort(400, "Invalid input!")


if __name__ == '__main__':
    api.run()
