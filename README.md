This repo is the source code for a python Flask backend service that supports a basic service catalog

It has 3 major API endpoints:
* /services

** Get all services stored in the backend
** It may have 3 optional parameters

*** `query`: input query to filter the results. The results only include services which name or description contains the query.
*** `page`: the number of pages to return
*** `page_length`: the number of cards returned in a single page. Default value is 12 if not specified.

** The return order is the reverse order of the created date

* /service/<service_id>

** Get a single service given a service_id
*** Return empty payload if no service has been found

* /add_service

** Add a single service with name and description to the backend storage
** It has 2 input parameters
*** `name`: the name of the service. This is required and can't be empty.
*** `description`: the description of the service. This is optional.


The API response format is defined in representation.py

Here are the steps to run the program and test:

* Install python flask (skip if you already have flask installed)

`$ pip install Flask`

* Start the server

`$ python api.py`

* Create new services

`curl -X POST -H "Content-Type: application/json" -d '{"name":"test11", "description": "This is test 11"}' localhost:5000/add_service`

`curl -X POST -H "Content-Type: application/json" -d '{"name":"test22", "description": "This is test 22"}' localhost:5000/add_service`

`curl -X POST -H "Content-Type: application/json" -d '{"name":"test33", "description": "This is test 33"}' localhost:5000/add_service`

* List all services

`curl http://localhost:5000/services`

This can be done in a browser as well

* List a specific service

`curl http://localhost:5000/service/<service_id>`

This can be done in a browser as well

TODO:

** Add more user authentication/authentication

** Build a real data storage

** Build a ID generation service

** Build add_version endpoint

** Edit existing Service/Version






