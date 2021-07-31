import utils


def test_add_retrieve_service():
    service_id = utils.add_service("test-name", "description-test")
    service = utils.get_service(service_id)

    assert service.name == "test-name"
    assert service.description == "description-test"


def test_get_all_services():
    # add 4 service as test data
    utils.add_service("test-1", "description-1")
    utils.add_service("test-2", "description-2")
    utils.add_service("test-1", "description-1")
    utils.add_service("test-1", "description-1")

    # verify services with same name and description can co-exist
    services, max_page = utils.get_services()
    assert len(services) == 4
    assert max_page == 0

    # verify no service from page 1(2nd page)
    services, max_page = utils.get_services(page=1)
    assert len(services) == 0
    assert max_page == 0

    # verify 2 services from page 1(2nd page) when page_length=2
    services, max_page = utils.get_services(page_length=2, page=1)
    assert len(services) == 2
    assert max_page == 1

    # verify 1 services from page 1(2nd page) when page_length=3
    services, max_page = utils.get_services(page_length=3, page=0)
    assert len(services) == 3
    assert max_page == 1

    # verify 1 services from page 1(2nd page) when page_length=3
    services, max_page = utils.get_services(page_length=3, page=1)
    assert len(services) == 1
    assert max_page == 1

    # verify filtering logic
    services, max_page = utils.get_services(query="random")
    assert len(services) == 0
    print max_page
    assert max_page == 0

    # verify search logic
    services, max_page = utils.get_services(query="test")
    assert len(services) == 4
    assert max_page == 0

    # verify search logic with UPPER CASE
    services, max_page = utils.get_services(query="TEST")
    assert len(services) == 4
    assert max_page == 0
