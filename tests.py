import resource
import requests
import json


def test_api_endpoints():

    # make sure to start the server before running this test

    resp = requests.get("http://localhost:5000/services")
    assert resp.status_code == 200
    resp = requests.get("http://localhost:5000/services?query=1234")
    assert resp.status_code == 200

    resp = requests.post("http://localhost:5000/add_service", data=json.dumps({"name":"name1", "description": "description1"}))

    assert resp.status_code == 200
    service_id = json.loads(resp.content)["service_id"]
    assert service_id

    resp = requests.get("http://localhost:5000/service/" + str(service_id))
    assert resp.status_code == 200
    assert json.loads(resp.content).get("name") == "name1"

    resp = requests.get("http://localhost:5000/services")
    assert resp.status_code == 200
    assert len(json.loads(resp.content).get("services")) == 1


def test_add_retrieve_service():
    service_id = resource.add_service("test-name", "description-test")
    service = resource.get_service(service_id)

    assert service.name == "test-name"
    assert service.description == "description-test"


def test_get_all_services():

    # add 4 service as test data
    resource.add_service("test-1", "description-1")
    resource.add_service("test-2", "description-2")
    resource.add_service("test-1", "description-1")
    resource.add_service("test-1", "description-1")

    # verify services with same name and description can co-exist
    services, max_page = resource.get_services()
    assert len(services) == 4
    assert max_page == 0

    # verify no service from page 1(2nd page)
    services, max_page = resource.get_services(page=1)
    assert len(services) == 0
    assert max_page == 0

    # verify 2 services from page 1(2nd page) when page_length=2
    services, max_page = resource.get_services(page_length=2, page=1)
    assert len(services) == 2
    assert max_page == 1

    # verify 1 services from page 1(2nd page) when page_length=3
    services, max_page = resource.get_services(page_length=3, page=0)
    assert len(services) == 3
    assert max_page == 1

    # verify 1 services from page 1(2nd page) when page_length=3
    services, max_page = resource.get_services(page_length=3, page=1)
    assert len(services) == 1
    assert max_page == 1

    # verify filtering logic
    services, max_page = resource.get_services(query="random")
    assert len(services) == 0
    print max_page
    assert max_page == 0

    # verify search logic
    services, max_page = resource.get_services(query="test")
    assert len(services) == 4
    assert max_page == 0

    # verify search logic with UPPER CASE
    services, max_page = resource.get_services(query="TEST")
    assert len(services) == 4
    assert max_page == 0


if __name__ == '__main__':
    test_api_endpoints()
    test_add_retrieve_service()
    test_get_all_services()