"""

This module defines the response for API
"""


class GetServicesResponse:
    @classmethod
    def get_response(cls, services, page, max_page):
        resp = {"services": []}

        for service in services:
            resp["services"].append({
                "service_id": service.service_id,
                "name": service.name,
                "description": service.description,
                "created_ts": service.created_ts,
                "number_versions": len(service.versions)
            })

        resp["page"] = page
        resp["max_page"] = max_page
        if page < max_page:
            resp["next_page"] = page + 1

        return resp


class GetServiceResponse:
    @classmethod
    def get_response(cls, service):
        if not service:
            return {}

        resp = {"service_id": service.service_id, "name": service.name, "description": service.description,
                "created_ts": service.created_ts, "versions": []}

        for version in service.versions:
            resp["versions"].append({
                "name": version.name,
                "version_id": version.version_id
            })

        return resp


class AddServiceResponse:
    @classmethod
    def get_response(cls, service_id):
        return {"service_id": service_id}
